from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'salarymanagement'

urlpatterns = [ 
    #URLs for student app
    path('home', views.HomeView.as_view(), name="home_view"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
    path('feature', views.FeatureView.as_view(), name="feature_view"),
    path('aboutus', views.AboutUsView.as_view(), name="about_us_view"),
]