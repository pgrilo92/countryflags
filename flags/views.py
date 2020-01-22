from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class FlagCreate(CreateView):
    model = Flag
    fields = '__all__'
    success_url = '/flags/'

class FlagUpdate(UpdateView):
    model = Flag
    fields = ['population', 'description']

class FlagDelete(DeleteView):
    model = Flag
    success_url = '/flags/'
