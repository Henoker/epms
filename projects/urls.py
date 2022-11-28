from django.urls import path 

from . import views

urlpatterns = [
    path("projects", views.projects, name="projects"),
    path("clients", views.clients, name="clients"),
    path('vendors', views.vendors, name='vendors'),
    path('invoices',views.invoices, name='invoices'),
    path('orders', views.orders, name='orders'),

    # Invoice create paths
    path('invoices/create',views.createInvoice, name='create-invoice'),
    path('invoices/create-build/<slug:slug>',views.createBuildInvoice, name='create-build-invoice'),
    path('invoices/delete/<slug:slug>',views.deleteInvoice, name='delete-invoice'),
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
    # Path for Orders
    path('updateOrder/<slug:slug>',views.updateOrder, name='update-order'),
    path('orders/delete/<slug:slug>',views.deleteOrder, name='delete-order'),

]
