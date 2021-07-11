from django.contrib import admin
from .models import Employee,Education,Skill,Experience,Project

# Register your models here.
admin.site.register([Employee,Education,Skill,Experience,Project])
