from django.urls import path

from .views import HomePageView, ProjectsPageView, DashboardPageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("projects/", ProjectsPageView.as_view(), name="projects"),
]
