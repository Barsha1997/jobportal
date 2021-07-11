from django import forms
from .models import Employeer


class EmployeerCreateForm(forms.ModelForm):
    companyName = forms.CharField(max_length=100, verbose_name="Company Name", db_column="Company_name")
    address = forms.CharField(max_length=100, verbose_name="Address")
    contactNo = forms.CharField(max_length=20, null=True, blank=True, db_column="contact_no")


    class Meta:
        model = Employeer
        exclude =['user',]