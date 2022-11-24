from django.contrib import admin
from .models import Client, Project

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ("clientName", "emailAddress", "phoneNumber", "addressLine1", "country")
class projectAdmin(admin.ModelAdmin):
    list_display = ("projectName", "startDate", "deadlineDate",  "quantity", "rate",  "project_manager", "status",)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project, projectAdmin)
