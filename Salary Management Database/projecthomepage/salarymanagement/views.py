from django.shortcuts import render
from django.views.generic import View
from .forms import *

# Create your views here.
class HomeView(View):
	def get(self, request):			
		return render(request,'home.html')

class FeatureView(View):
	def get(self, request):		
		return render(request,'feature.html')

class DashboardView(View):
	def get(self, request):	
		employers = Employer.objects.all()
		employees = Employee.objects.all()

		"""
		> pass the view to template
		> may contain 1++ vars
		"""
		context = {
			'employer': employers,
			'employee': employees
		}
		return render(request,'dashboard.html', context)
        
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