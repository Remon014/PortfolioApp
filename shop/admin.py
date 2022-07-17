from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("__str__", "current_price","Stock", "created_at", "image"  )
    list_editable = ("current_price","Stock",)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("__str__", "Subject", "Email", "time")

admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)