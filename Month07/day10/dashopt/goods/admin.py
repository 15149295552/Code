from django.contrib import admin
from goods.models import SKU
from django.core.cache import caches


class SKUManager(admin.ModelAdmin):
    list_display = ["id", "name", "price", "stock", "sales"]
    list_editable = ["price"]

    def save_model(self, request, obj, form, change):
        # 1.更新mysql中数据
        super().save_model(request, obj, form, change)
        # 2.清除redis缓存
        key = f"gd{obj.id}"
        caches["detail"].delete(key)
        print("更新数据时,Redis中缓存清除~~")

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        caches["detail"].delete(f"gd{obj.id}")


admin.site.register(SKU, SKUManager)