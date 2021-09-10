from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HomeView(View):
	def get(self, request):					
		return render(request,'home.html')

class FeatureView(View):
	def get(self, request):					
		return render(request,'feature.html')

class DashboardView(View):
	def get(self, request):					
		return render(request,'dashboard.html')
        
class AboutUsView(View):
	def get(self, request):					
		return render(request,'aboutus.html')

class SignInView(View):
	def get(self, request):					
		return render(request,'signin.html')

class SignUpView(View):
	def get(self, request):					
		return render(request,'signup.html')

class ContactUsView(View):
	def get(self, request):					
		return render(request,'contactus.html')