from django.urls import path
from.views import create,dashboard

urlpatterns=[
    path('create/',create,name='employee_create'),
    path('dashboard/', dashboard, name='empdashboard')

]