from django.contrib import admin
from .models import Employeer,Job,Application

# Register your models here.
admin.site.register([Employeer,Job,Application])