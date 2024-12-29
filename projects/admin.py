from django.contrib import admin
from .models import Client, Project, Order, Invoice, Job, PurchaseOrder, Rating, Settings, Quotation, Request, Vendor

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ("clientName", "emailAddress", "phoneNumber", "addressLine1", "country")
class projectAdmin(admin.ModelAdmin):
    list_display = ("projectName", "project_manager", "status", "client", "budgetedamount")
class OrderAdmin(admin.ModelAdmin):
    list_display = ("project", "OrderDate", "clientDeadline", "quantity", "price", "source_languages","target_languages")
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type', 'project_manager', 'assigned_to', 'status', 'purchaseOrder', 'total_price')
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, projectAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice)
admin.site.register(Job, JobAdmin)
admin.site.register(PurchaseOrder)
admin.site.register(Rating)
admin.site.register(Settings)
admin.site.register(Quotation)
admin.site.register(Request)
admin.site.register(Vendor)
