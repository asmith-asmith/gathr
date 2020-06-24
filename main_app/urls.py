from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),

    path('products/', views.ProductList.as_view(), name="product_index"),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/create/', views.ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),

    path('causes/', views.cause_index, name="cause_index"),
    path('causes/<int:pk>/', views.CauseDetail.as_view(), name="cause_detail"),
    path('causes/create/', views.CauseCreate.as_view(), name="cause_create"),
    path('causes/<int:pk>/update/', views.CauseUpdate.as_view(), name="cause_update"),
    path('causes/<int:pk>/delete/', views.CauseDelete.as_view(), name="cause_delete"),

    path('profile/<int:user_id>/', views.user_detail, name='user_detail'),

    path('cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/<int:order_id>/update', views.order_form, name='order_update'),

    path('products/<int:product_id>/add_photo/', views.add_product_photo, name='add_product_photo'),
    # path('causes/<int:cause_id>/add_photo/', views.add_cause_photo, name='add_cause_photo'),
    # path('users/<int:user_id>/add_photo/', views.add_user_photo, name='add_user_photo'),
]