from django.contrib import admin
from django.core.cache import caches
from goods.models import SKU


class SKUManager(admin.ModelAdmin):
    list_display = ["id", "name", "price", "stock", "sales"]

    def save_model(self, request, obj, form, change):
        # 1.更新MySQL数据(源码逻辑)
        super().save_model(request, obj, form, change)
        # 2.清除Redis缓存
        key = f"gd_{obj.id}"
        caches["detail"].delete(key)
        print("更新数据时,详情页缓存清除啦~~~")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        key = f"gd_{obj.id}"
        caches["detail"].delete(key)
        print("删除数据时，详情页缓存清除啦~~~")


admin.site.register(SKU, SKUManager)




