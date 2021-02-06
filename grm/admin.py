from django.contrib import admin
from .models import *

# Register your models here.
class CustomerList(admin.ModelAdmin):
    list_display = ('cust_name', 'email', 'ending_date','additional_comment')
    list_filter = ('cust_name', 'ending_date')
    search_fields = ('cust_name',)
    ordering = ['cust_name']

#admin.site.register(Customer, CustomerList)
admin.site.register(Gymmember, CustomerList)

class RentalList(admin.ModelAdmin):
   list_display = ( 'cust_name', 'Gymitem_name', 'return_date')
   list_filter = ('cust_name','Gymitem_name', 'return_date')
  # search_fields = ('Patron_name','Book_name', )
   ordering = ['cust_name']

admin.site.register(Rental, RentalList)