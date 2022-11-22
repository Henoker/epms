from django.urls import path

from .views import HomePageView, ProjectsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("projects/", ProjectsPageView.as_view(), name="projects")
]
