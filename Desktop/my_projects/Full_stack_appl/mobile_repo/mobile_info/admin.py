from django.contrib import admin
from .models import Mobile_List, Mobile_Features
# Register your models here.
class MobileAdmin(admin.ModelAdmin):
    list_display = ('id','brand_name','price')
class FeaturesAdmin(admin.ModelAdmin):
    list_display=('id','storage','processor','battery')

admin.site.register(Mobile_List,MobileAdmin)
admin.site.register(Mobile_Features,FeaturesAdmin)