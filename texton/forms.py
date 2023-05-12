from django import forms
from texton.models import Student,Employer

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'age', 'phone_number']


class EmployeeForm(forms.Form):
      firstname= forms.CharField(label="Enter Firstname", max_length=50)
      lastname= forms.CharField(label="Enter Lastname", max_length=50)
      age= forms.IntegerField(label="Enter Age",)
      phone_number= forms.IntegerField(label="Enter Phone_number",)




