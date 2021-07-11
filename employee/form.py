from django import forms
from .models import Employee, Skill


class EmployeeCreateForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="First Name")
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Last Name")
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Address")
    DOB = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'Date'}),
                          label="Date of birth")

    class Meta:
        model = Employee
        exclude = ['user', ]


class AddSkillForm(forms.ModelForm):
    skillName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Skill Name")
    level = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="level")

    class Meta:
        model = Skill
        exclude = ['employee', ]


class ChangeProfileImageForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['profile', ]


class AboutEditForm(forms.ModelForm):
    aboutme = forms.CharField(widget=forms.Textarea(attrs={'id': "aboutme", 'class': 'form-control', 'rows': 5, 'readonly': True}))

    class Meta:
        model = Employee
        fields = ['aboutme', ]
