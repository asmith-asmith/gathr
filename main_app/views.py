from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required #@login_required  -- add this to functions
from django.contrib.auth.mixins import LoginRequiredMixin #LoginRequiredMixin, -- add this in CBV parameter
from .models import Product, Cause


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProductList(ListView):
  model = Product

class ProductDetail(DetailView):
  model = Product

class ProductCreate(CreateView):
  model = Product
  fields = '__all__'

class ProductUpdate(UpdateView):
  model = Product
  fields = '__all__'

class ProductDelete(DeleteView):
  model = Product
  success_url = '/products/'

class CauseList(ListView):
  model = Cause

class CauseDetail(DetailView):
  model = Cause

class CauseCreate(CreateView):
  model = Cause
  fields = '__all__'

class CauseUpdate(UpdateView):
  model = Cause
  fields = '__all__'

class CauseDelete(DeleteView):
  model = Cause
  success_url = '/cause/'