from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required #@login_required  -- add this to functions
from django.contrib.auth.mixins import LoginRequiredMixin #LoginRequiredMixin, -- add this in CBV parameter
from django.utils import timezone
from django.db.models.signals import post_save
from .models import Product, Cause, Profile, User, Order, ProductPhoto, CausePhoto, UserPhoto
from .forms import OrderForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'learning-catcollector-aws-s3'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def emptycart(request):
  return render(request, 'empty.html')

def success(request):
  return render(request, 'success.html')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProductList(ListView):
  queryset = Product.objects.filter(Q(size='Small') | Q(size='7') )


def product_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  other_prod = Product.objects.filter(Q(name=product.name) & ~Q(size=product.size))
  # order_form = OrderForm()
  return render(request, 'main_app/product_detail.html', {'product': product, 'other_prod': other_prod})

# class ProductDetail(DetailView):
#   model = Product

class ProductCreate(LoginRequiredMixin, CreateView):
  model = Product
  fields = '__all__'

class ProductUpdate(LoginRequiredMixin, UpdateView):
  model = Product
  fields = '__all__'

class ProductDelete(LoginRequiredMixin, DeleteView):
  model = Product
  success_url = '/products/'


def cause_index(request):
  causes = Cause.objects.all()
  return render(request, 'main_app/cause_list.html', {'cause_list': causes})

class CauseDetail(DetailView):
  model = Cause

class CauseCreate(LoginRequiredMixin, CreateView):
  model = Cause
  fields = '__all__'

class CauseUpdate(LoginRequiredMixin, UpdateView):
  model = Cause
  fields = '__all__'

class CauseDelete(LoginRequiredMixin, DeleteView):
  model = Cause
  success_url = '/causes/'

@login_required
def user_detail(request, user_id):
  user = User.objects.get(id=user_id)
  # user = User.objects.get(id=profile.user)
  return render(request, 'main_app/user_detail.html', {'user': user})

@login_required
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

@login_required
def cart_detail(request):
  not_ordered = request.user.order_set.filter(ordered=False).exists()
  if not_ordered:
    order = Order.objects.get(user=request.user, ordered=False)
    return render(request, 'main_app/order_detail.html', {'order': order})
  else:
    return render(request, 'empty.html') 

@login_required
def order_form(request, order_id):
  order = Order.objects.get(id=order_id)
  return render(request, 'main_app/order_form.html', {'order': order})

@login_required
def order_confirm(request, order_id):
  order_query = Order.objects.filter(user=request.user, ordered=False)
  order = order_query[0]
  order.ordered = True
  order.save()
  return render(request, 'success.html')

@login_required
def order_empty(request, order_id):
  order = Order.objects.get(id=order_id)
  for prod in order.product.all():
    order.product.remove(prod.id)
  return redirect('product_index')

@login_required
def add_product_photo(request, product_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = ProductPhoto(url=url, product_id=product_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('product_detail', product_id=product_id)

@login_required
def add_cause_photo(request, cause_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = CausePhoto(url=url, cause_id=cause_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('cause_detail', pk=cause_id)