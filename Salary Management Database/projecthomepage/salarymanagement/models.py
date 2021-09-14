from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Employer(models.Model):
    employer_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city = models.CharField(max_length=20)

    class meta:
        db_table = 'tblEmployer'

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    age = models.IntegerField()
    contact_num = models.CharField(max_length=20)
    year_hired = models.DateField()
    hours_worked = models.IntegerField()
    overtime = models.IntegerField()
    hours_late = models.IntegerField()
    days_absent = models.IntegerField()

    class meta:
        db_table = 'tblEmployee'

class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class meta:
        db_table = 'tblSalary'


"""
Employee - employeeID, name, city, age, contact, year hired, hours worked, overtime
Salary - salaryID, amount
Attendance - employeeID, hours late, days absent

BUSINESS RULES
An EMPLOYER can manage one or more SALARY for each EMPLOYEE
▪ Attributes of EMPLOYER: Employer_ID, Name, City
✓ An EMPLOYEE only has one EMPLOYER who handles his/her SALARY.
▪ Attributes of EMPLOYEE: Employee_ID, Name, City, Age, Telephone, Year_Hired,
Hours_Worked, Overtime
✓ An EMPLOYEE only has one SALARY
▪ Attributes of SALARY: Salary_ID, Amount
✓ Each EMPLOYEE has ATTENDANCE:
▪ Attributes of ATTENDANCE: Employee_ID, Hours_Late, Days_Absent
"""