from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hello/<int:result>/',views.hello,name='hello'),
]