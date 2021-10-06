from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import *
from django.http import JsonResponse, request

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
		city = City.objects.all()

		"""
		> pass the view to template
		> may contain 1++ vars
		"""
		context = {
			'employer': employers,
			'employee': employees,
			'city': city
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
		return render(request, 'addemployer.html', {'city' : City.objects.all()})

	def post(self, request):
		form = EmployerForm(request.POST)
	
		fname = request.POST.get("firstname")
		lname = request.POST.get("lastname")
		city = request.POST.get("city")

		form = Employer(firstname = fname, lastname = lname, city_id_id = city)
		form.save()

		return redirect('salarymanagement:dashboard_view')
	
		#	return HttpResponse('not valid')

class AddEmployeeView(View):
	def get(self, request):
		return render(request, 'addemployee.html', {'employers' : Employer.objects.all(), 'city' : City.objects.all()})

	def post(self, request):
		form = EmployeeForm(request.POST)

		fname = request.POST.get("firstname")
		lname = request.POST.get("lastname")
		city = request.POST.get("city")
		age = request.POST.get("age")
		cnumber = request.POST.get("contact")
		employer_id = request.POST.get("employerid")
		form = Employee(firstname = fname, lastname = lname, city_id_id = city, age = age, contact_num = cnumber, employer_id_id = employer_id)
		form.save()

		return redirect('salarymanagement:dashboard_view')

class AddSalaryView(View):
	def get(self, request):
		return render(request, 'addsalary.html')