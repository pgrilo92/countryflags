from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flag, President, Language
from .forms import PresidentForm, LanguageForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

@login_required
def flags_detail(request, flag_id):
    flag = Flag.objects.get(id=flag_id)
    languages_not_in_flag = Language.objects.exclude(id__in = flag.languages.all().values_list('id'))
    president_form = PresidentForm()
    return render(request, 'flags/detail.html', {
        'flag': flag, 
        'president_form': president_form,
        'languages': languages_not_in_flag, 
        })

@login_required
def add_president(request, flag_id):
    form = PresidentForm(request.POST)
    if form.is_valid():
        new_president = form.save(commit=False)
        new_president.flag_id = flag_id
        new_president.save()
    return redirect('detail', flag_id=flag_id)

@login_required 
def delete_president(request, president_id):
    president = President.objects.get(pk=president_id)
    president.delete()
    return redirect(f'/flags/{president.flag_id}')

@login_required    
def flags_index(request):
    flags = Flag.objects.filter(user=request.user)
    return render(request, 'flags/index.html', {'flags': flags})

def about(request):
    return render(request, 'about.html')


class FlagCreate(LoginRequiredMixin, CreateView):
    model = Flag
    fields = ['country', 'capital_city', 'flag_img', 'continent', 'population', 'description']
    success_url = '/flags/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FlagUpdate(LoginRequiredMixin, UpdateView):
    model = Flag
    fields = ['population', 'description']

class FlagDelete(LoginRequiredMixin, DeleteView):
    model = Flag
    success_url = '/flags/'

def language_index(request):
    form = LanguageForm()
    languages = Language.objects.all()
    return render(request, 'languages/index.html', {'languages':languages, 'language_form':form})

def create_language(request):
    form = LanguageForm(request.POST)
    if form.is_valid():
        language = form.save()
        return redirect('/languages')

def add_language_to_flag(request, flag_id, language_id):
    Flag.objects.get(id=flag_id).languages.add(language_id)
    return redirect('detail', flag_id=flag_id)

def remove_language_to_flag(request, flag_id, language_id):
    Flag.objects.get(id=flag_id).languages.remove(language_id)
    return redirect('detail', flag_id=flag_id)