from django.urls import path 

from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("projects", views.projects, name="projects"),
    path("clients", views.clients, name="clients"),
    path('vendors', views.vendors, name='vendors'),
    path('invoices',views.invoices, name='invoices'),
    path('orders', views.orders, name='orders'),
    path('purchaseOrders',views.purchaseOrders, name='purchase-orders'),
    path('jobs', views.jobs, name='jobs'),
    path('rating', views.rating, name='rating'),

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

    # Po create paths
    path('purchaseOrders/create',views.createPo, name='create-po'),
    path('purchaseOrders/create-build/<slug:slug>',views.createBuildPo, name='create-build-po'),
    path('purchaseOrders/delete/<slug:slug>',views.deletePo, name='delete-po'),

     # Path for Orders
    path('updateJob/<slug:slug>',views.updateJob, name='update-job'),
    path('jobs/delete/<slug:slug>',views.deleteJob, name='delete-job'),

    #Company Settings Page
    path('company/settings',views.companySettings, name='company-settings'),

    #PDF and EMAIL Paths
    path('invoices/view-pdf/<slug:slug>',views.viewPDFInvoice, name='view-pdf-invoice'),
    path('invoices/view-document/<slug:slug>',views.viewDocumentInvoice, name='view-document-invoice'),
    # path('invoices/email-document/<slug:slug>',views.emailDocumentInvoice, name='email-document-invoice'),
    path('invoices/view-po/<slug:slug>',views.viewDocumentPO, name='view-document-po'),
    path('invoices/view-POpdf/<slug:slug>',views.viewPDFPO, name='view-pdf-po'),


    path('addRating',views.addRating, name='add-rating'),

]
