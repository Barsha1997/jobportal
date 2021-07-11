from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=100, verbose_name="First Name", db_column="first_name")
    lastname = models.CharField(max_length=100, verbose_name="Last Name", db_column="Last_name")
    address = models.CharField(max_length=100, verbose_name="Address")
    contactNo = models.CharField(max_length=10)
    DOB = models.DateField(null=True, blank=True)
    profile = models.ImageField(blank=True, null=True, upload_to='profile/')
    aboutme = models.TextField(blank=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.firstname


class Education(models.Model):
    course = models.CharField(max_length=200, verbose_name="Course name(ex Bsc csit)")
    university = models.CharField(max_length=100, verbose_name="University", null=True, blank=True)
    joinedYear = models.CharField(max_length=4, db_column="joined_year")
    passYear = models.DateField(max_length=4, db_column="passed_year", null=True, blank=True)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = "education"

    def __str__(self):
        return self.course


class Project(models.Model):
    projectName = models.CharField(max_length=200, verbose_name="project name", db_column="project_name")
    description = models.TextField(null=True, blank=True)
    projectLink = models.URLField(null=True, blank=True, verbose_name="Project link", db_column="Project_Link")
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.projectName

    class Meta:
        db_table = "project"


class Skill(models.Model):
    skillName = models.CharField(max_length=30, db_column="skill_name")
    level = models.IntegerField(verbose_name="level of Knowledge out of 100")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.skillName

    class Meta:
        db_table = "skill"
        unique_together = ('skillName', 'employee')


class Experience(models.Model):
    company = models.CharField(max_length=100)
    JoinedYear = models.DateField(max_length=4, db_column="joined_year", verbose_name="company joined year")
    leftYear = models.DateField(max_length=4, db_column="Left_year", verbose_name="company left year", null=True,
                                blank=True)
    JobTitle = models.CharField(max_length=100, db_column="Job_title")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

    class Meta:
        db_table = "Experience"


