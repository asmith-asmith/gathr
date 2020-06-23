from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required #@login_required  -- add this to functions
from django.contrib.auth.mixins import LoginRequiredMixin #LoginRequiredMixin, -- add this in CBV parameter
from .models import Product, Cause, Profile, User
from .forms import OrderForm


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
      # p = Profile(user=user.user_id, causes=null)
      # p.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProductList(ListView):
  model = Product


def product_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  order_form = OrderForm()
  return render(request, 'main_app/product_detail.html', {'product': product, 'order_form': order_form})

# class ProductDetail(DetailView):
#   model = Product

class ProductCreate(CreateView):
  model = Product
  fields = '__all__'

class ProductUpdate(UpdateView):
  model = Product
  fields = '__all__'

class ProductDelete(DeleteView):
  model = Product
  success_url = '/products/'


def cause_index(request):
  causes = Cause.objects.all()
  return render(request, 'main_app/cause_list.html', {'cause_list': causes})


# class CauseList(ListView):
#   model = Cause

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
  success_url = '/causes/'


def user_detail(request, user_id):
  user = User.objects.get(id=user_id)
  # user = User.objects.get(id=profile.user)
  return render(request, 'main_app/user_detail.html', {'user': user})
