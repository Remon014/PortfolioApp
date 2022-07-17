from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    path('productdetail/', views.productdetail, name='productdetail'),
    path('checkout/', views.checkout, name='checkout'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('login_register/', views.login_register, name='login_register'),
]
