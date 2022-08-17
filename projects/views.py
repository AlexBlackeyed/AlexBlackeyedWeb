from django.shortcuts import render

from .models import Project


data = Project.objects.all()
def projects(request, flare=None):
    new_data = [d for d in data if flare in d.flare]
    if flare is None:
        return render(request, 'projects.html', {'projectss': data})
    else:
        return render(request, 'projects.html', {'projectss': new_data})