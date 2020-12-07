from django.urls import path
from . import views

app_name='main'
urlpatterns=[
    path('',views.Home,name='home'),
    path('product',views.product,name='product'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('team',views.team,name='team'),
    path('contact',views.contact,name='contact')

]