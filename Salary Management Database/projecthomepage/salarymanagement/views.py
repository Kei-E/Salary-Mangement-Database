from django.http.response import HttpResponse
from django.shortcuts import redirect, render
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

class AddEmployerView(View):
	def get(self, request):
		return render(request, 'addemployer.html')

	def post(self, request):
		form = EmployerForm(request.POST)

		if form.is_valid():
			fname = request.POST.get("firstname")
			lname = request.POST.get("lastname")
			city = request.POST.get("city")
			form = Employer(firstname = fname, lastname = lname, city = city)
			form.save()

			return redirect('salarymanagement:dashboard_view')
		else:
			return HttpResponse('not valid')
			
		

class AddEmployeeView(View):
	def get(self, request):
		return render(request, 'addemployee.html')

class AddSalaryView(View):
	def get(self, request):
		return render(request, 'addsalary.html')