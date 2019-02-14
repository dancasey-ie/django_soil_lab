from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
# TabularInline subclass defines the template used to render the order in the admin interface
class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )

admin.site.register(Order, OrderAdmin)