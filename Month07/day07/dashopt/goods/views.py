from django.conf import settings
from django.http import JsonResponse
from django.views import View
from goods.models import Catalog, SPU, SKU, SKUImage, SPUSaleAttr, SaleAttrValue, SKUSpecValue
from utils.cache_dec import cache_check


class GoodsIndexView(View):
    def get(self, request):
        """
        首页展示视图逻辑
        {"code":200,"data":[],"base_url":"xxx"}
        """
        print("\033[31mdata from mysql~\033[0m")
        data = []
        all_cata = Catalog.objects.all()
        for cata in all_cata:
            sku_list = []
            # ER图: Catalog -> SPU -> SKU
            # spus: <QuerySet [<>,<>,<>,...]>
            spus = SPU.objects.filter(catalog=cata)
            skus = SKU.objects.filter(spu__in=spus)[:3]
            for sku in skus:
                sku_dict = {
                    "skuid": sku.id,
                    "caption": sku.caption,
                    "name": sku.name,
                    "price": sku.price,
                    "image": str(sku.default_image_url)
                }
                sku_list.append(sku_dict)

            cata_dict = {
                "catalog_id": cata.id,
                "catalog_name": cata.name,
                "sku": sku_list
            }
            data.append(cata_dict)

        return JsonResponse({"code": 200, "data": data, "base_url": settings.PIC_URL})


class GoodsDetailView(View):
    # @cache_page(30, cache="detail")
    @cache_check(expire=60, cache="detail", key_prefix="gd")
    def get(self, request, sku_id):
        """
        详情页展示视图逻辑
        {"code":200, "data":{}, "base_url":"xx"}
        """
        try:
            sku = SKU.objects.get(id=sku_id, is_launched=True)
        except Exception as e:
            return JsonResponse({"code": 10200, "error": "该商品已下架!"})

        data = {}
        # 类1:类别id 类别name
        cata = sku.spu.catalog
        data["catalog_id"] = cata.id
        data["catalog_name"] = cata.name

        # 类2：SKU
        data["name"] = sku.name
        data["caption"] = sku.caption
        data["price"] = sku.price
        data["image"] = str(sku.default_image_url)
        data["spu"] = sku.spu.id

        # 类3：详情图片
        img_query = SKUImage.objects.filter(sku=sku)
        data["detail_image"] = img_query[0].image if img_query else ""

        # 类4：销售属性
        attr_query = SPUSaleAttr.objects.filter(spu=sku.spu)
        data["sku_sale_attr_id"] = [i.id for i in attr_query]
        data["sku_sale_attr_names"] = [i.name for i in attr_query]

        # 类5：销售属性值
        value_query = sku.sale_attr_value.all()
        data["sku_sale_attr_val_id"] = [i.id for i in value_query]
        data["sku_sale_attr_val_names"] = [i.name for i in value_query]

        # 销售属性和销售属性值的对应关系
        id_dict = {}
        name_dict = {}
        id_list = [i.id for i in attr_query]
        for id in id_list:
            item_query = SaleAttrValue.objects.filter(spu_sale_attr=id)
            id_dict[id] = [i.id for i in item_query]
            name_dict[id] = [i.name for i in item_query]

        data["sku_all_sale_attr_vals_id"] = id_dict
        data["sku_all_sale_attr_vals_name"] = name_dict

        # 类6和类7：规格属性名和规格属性值
        spec = {}
        spec_query = SKUSpecValue.objects.filter(sku=sku)
        for sp in spec_query:
            key = sp.spu_spec.name
            value = sp.name
            spec[key] = value

        data["spec"] = spec

        return JsonResponse({"code": 200, "data": data, "base_url": settings.PIC_URL})







