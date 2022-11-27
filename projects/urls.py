from django.urls import path 

from . import views

urlpatterns = [
    path("projects", views.projects, name="projects"),
    path("clients", views.clients, name="clients"),
    path('vendors', views.vendors, name='vendors'),
    # Update and delete a client
    path('updateClient/<slug:slug>',views.updateClient, name='update-client'),
    path('clients/delete/<slug:slug>',views.deleteClient, name='delete-client'),
    # Update and delete a project
    path('updateProject/<slug:slug>',views.updateProject, name='update-project'),
    path('addProject',views.addProject, name='add-project'),
    path('projects/delete/<slug:slug>',views.deleteProject, name='delete-project'),
    #Update and Delete a Vendor
    path('vendors/delete/<slug:slug>',views.deleteVendor, name='delete-vendor'),
    path('updateVendor/<slug:slug>',views.updateVendor, name='update-vendor'),

]
