from django.contrib import admin

# Register your models here.
from .models import Gymitem


class GymitemList(admin.ModelAdmin):
    list_display = ( 'Gymitem_name', 'Gymitem_id' , 'Gymitem_description','Gymitem_category')
    list_filter = ( 'Gymitem_name', 'Gymitem_category')
    search_fields = ('Gymitem_name', )
    ordering = ['Gymitem_name']


admin.site.register(Gymitem,GymitemList)