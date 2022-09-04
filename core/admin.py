
from django.contrib import admin
from core.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("name", "price", "digital", )
    list_filter= ("name", "price")
    resource_class=ProductResource
    search_fields=("name", "price", "digital")

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order

class OrderAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("customer", "date_ordered", "complete", )
    list_filter= ("customer", "date_ordered")
    resource_class = OrderResource
    search_fields=("customer", "date_ordered")


class OrderItemResource(resources.ModelResource):
    class Meta:
        model = OrderItem

class OrderItemAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("product", "order", "quantity", "date_added" )
    list_filter= ("product", "order", "date_added")
    resource_class = OrderItemResource
    search_fields=("product", "order")

class ShippingAddressResource(resources.ModelResource):
    class Meta:
        model = ShippingAddress

class ShippingAddressAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("customer", "order", "address", "city", "state", "zipcode", "date_added")
    list_filter= ("customer", "order", "city", "date_added")
    resource_class = ShippingAddressResource
    search_fields=("customer", "order", "city", "date_added")


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)