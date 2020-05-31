from django.shortcuts import render, get_object_or_404
from .models import Project 
from .models import Certificates

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'project/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project':project
    }
    return render(request, 'project/detail.html', context)


def index(request):
    certificates = Certificates.objects.all()
    context = {
        'certificates':certificates
    }
    return render(request, 'project/index.html', context)

def details(request, certificates_id):
    certificates = get_object_or_404(Certificates , id=certificates_id)
    context = {
        'certificates':certificates
    }
    return render(request, 'project/detail.html', context)







