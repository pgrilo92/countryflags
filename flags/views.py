from django.shortcuts import render
from .models import Flag

def home(request):
    return render(request, 'home.html')

def flags_detail(request, flag_id):
    flag = Flag.objects.get(id=flag_id)
    return render(request, 'flags/detail.html', {'flag': flag})
    
def flags_index(request):
    flags = Flag.objects.all()
    return render(request, 'flags/index.html', {'flags': flags})

def about(request):
    return render(request, 'about.html')