from django.shortcuts import render
from .forms import EmployeerCreateForm


# Create your views here.
def create(request):
    form = EmployeerCreateForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'employeer/create.html', context)
