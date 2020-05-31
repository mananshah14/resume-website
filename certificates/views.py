from django.shortcuts import render, get_object_or_404
from .models import Certificates

# Create your views here.
def index(request):
    certificates = Certificates.objects.all()
    context = {
        'certificates':certificates
    }
    return render(request, 'project/index.html', context)

def detail(request, certificates_id):
    certificates = get_object_or_404(Certificates , id=certificates_id)
    context = {
        'certificates':certificates
    }
    return render(request, 'project/detail.html', context)

# Create your views here.
