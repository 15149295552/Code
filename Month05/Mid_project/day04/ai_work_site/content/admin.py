from django.contrib import admin
from .models import Topic

# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title','category','limit','created_time','click_count','recommend','author')
    list_filter = ['category','limit']
    search_fields = ['title','author']

    fieldsets = (
        (None,{"fields":('category','limit')}),
        ('编辑',{'fields':('title','introduce','content','author')}),
        ('其他',{'fields':('click_count','recommend')})
    )

