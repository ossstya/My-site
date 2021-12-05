from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.works, name='works'),
    path('work/<int:pk>', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]