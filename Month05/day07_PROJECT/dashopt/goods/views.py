from django.conf import settings
from django.views import View
from django.http import JsonResponse

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
        cata_query = Catalog.objects.all()
        for cata in cata_query:
            # Catalog -> SPU -> SKU
            # 代码第2步
            spu_query = SPU.objects.filter(catalog=cata)
            sku_query = SKU.objects.filter(spu__in=spu_query)[:3]

            sku_list = []
            for sku in sku_query:
                sku_dict = {
                    "skuid": sku.id,
                    "caption": sku.caption,
                    "name": sku.name,
                    "price": sku.price,
                    "image": str(sku.default_image_url)
                }
                sku_list.append(sku_dict)

            # 代码第1步
            cata_dict = {
                "catalog_id": cata.id,
                "catalog_name": cata.name,
                "sku": sku_list
            }
            data.append(cata_dict)

        result = {
            "code": 200,
            "data": data,
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)


class GoodsDetailView(View):
    @cache_check(expire=888, cache="detail", key="gd_")
    def get(self, request, sku_id):
        """
        详情页展示视图逻辑
        {"code":200,"data":{},"base_url":""}
        """
        print("\033[32mdata from mysql\033[0m")
        data = {}
        try:
            sku = SKU.objects.get(id=sku_id, is_launched=True)
        except Exception as e:
            return JsonResponse({"code": 10200, "error": "该商品已下架"})

        # 类1:类别id 类别name
        #     SKU -> SPU -> Catalog
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
        if img_query:
            data["detail_image"] = str(img_query[0].image)
        else:
            data["detail_image"] = ""

        # 类4：销售属性
        attr_query = SPUSaleAttr.objects.filter(spu=sku.spu)

        data["sku_sale_attr_id"] = [i.id for i in attr_query]
        data["sku_sale_attr_names"] = [i.name for i in attr_query]

        # 类5：销售属性值
        value_query = sku.sale_attr_value.all()
        data["sku_sale_attr_val_id"] = [i.id for i in value_query]
        data["sku_sale_attr_val_names"] = [i.name for i in value_query]

        # 销售属性和销售属性值的对应关系
        sku_all_sale_attr_vals_id = {}
        sku_all_sale_attr_vals_name = {}

        id_list = [i.id for i in attr_query]
        for attr_id in id_list:
            # 找到attr_id销售属性对应的销售属性值的集合
            sale_value_query = SaleAttrValue.objects.filter(spu_sale_attr_id=attr_id)
            # 创建键值对
            sku_all_sale_attr_vals_id[attr_id] = [i.id for i in sale_value_query]
            sku_all_sale_attr_vals_name[attr_id] = [i.name for i in sale_value_query]

        data["sku_all_sale_attr_vals_id"] = sku_all_sale_attr_vals_id
        data["sku_all_sale_attr_vals_name"] = sku_all_sale_attr_vals_name

        # 类6和类7：规格属性名和规格属性值
        spec = {}
        spec_value_query = SKUSpecValue.objects.filter(sku=sku)
        for spec_value in spec_value_query:
            key = spec_value.spu_spec.name
            spec[key] = spec_value.name

        data["spec"] = spec

        result = {
            "code": 200,
            "data": data,
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)


