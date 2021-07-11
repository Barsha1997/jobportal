from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee


# Create your models here.

class Employeer(models.Model):
    companyName = models.CharField(max_length=100, verbose_name="Company Name", db_column="Company_name")
    address = models.CharField(max_length=100, verbose_name="Address")
    contactNo = models.CharField(max_length=20, null=True, blank=True, db_column="contact_no")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.companyName

    class Meta:
        db_table = "employeer"


class Job(models.Model):
    title = models.CharField(max_length=200, verbose_name="Job title")
    description = models.TextField(null=True, blank=True)
    qualification = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    employer = models.ForeignKey(Employeer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "job"


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    coverLetter = models.TextField(blank=True, null=True)
    appliedDate = models.DateField()

    def __str__(self):
        return self.job.title

    class Meta:
        db_table = "application"
        unique_together = ('job', 'employee')
