"""projecthomepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from salarymanagement import views

app_name = 'salarymanagement'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.HomeView.as_view(), name="home_view"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
    path('feature', views.FeatureView.as_view(), name="feature_view"),
    path('aboutus', views.AboutUsView.as_view(), name="about_us_view"),
    path('signin', views.SignInView.as_view(), name="sign_in_view"),
    path('signup', views.SignUpView.as_view(), name="sign_up_view"),
    path('contactus', views.ContactUsView.as_view(), name="contact_us_view"),
]