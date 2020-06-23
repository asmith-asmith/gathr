from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required #@login_required  -- add this to functions
from django.contrib.auth.mixins import LoginRequiredMixin #LoginRequiredMixin, -- add this in CBV parameter
from .models import Product, Cause, Profile, User, Order
from django.utils import timezone
# from .forms import 


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
  # order_form = OrderForm()
  return render(request, 'main_app/product_detail.html', {'product': product})

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


def add_cart(request, product_id):
  print(product_id)
  order_query = Order.objects.filter(user=request.user, ordered=False)
  product1 = Product.objects.get(id=product_id)
  if order_query.exists():
    order = order_query[0]
    if order.product.filter(id = product_id).exists():
      pass
    else:
      order.product.add(product1)
  else:
    ordered_date = timezone.now()
    order = Order.objects.create(user=request.user, ordered_date=ordered_date)
    order.product.add(product1)
  return render(request, 'main_app/order_detail.html', {'order': order})

def cart_detail(request):
  order = Order.objects.get(user=request.user)
  return render(request, 'main_app/order_detail.html', {'order': order})