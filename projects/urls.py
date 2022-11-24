from django.urls import path 

from . import views

urlpatterns = [
    path("projects", views.projects, name="projects"),
    path("clients", views.clients, name="clients"),
    # Update a client
    path('updateClient/<slug:slug>',views.updateClient, name='update-client'),
    path('clients/delete/<slug:slug>',views.deleteClient, name='delete-client'),
]
