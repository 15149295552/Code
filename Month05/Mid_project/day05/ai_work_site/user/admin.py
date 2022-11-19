from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import  UserAdmin

# admin.site.register(UserProfile,UserAdmin)

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ('username','nickname','email','phone','created_time')
    list_filter = ['username','is_staff']
    search_fields = ['username','phone']

    fieldsets = (
        (None,{"fields":('username','password','email')}),
        ('信息',{'fields':('nickname','avatar','sign','info','first_name','last_name')}),
        ('权限',{'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('时间',{'fields':('last_login','date_joined')})
    )
