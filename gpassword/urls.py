from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('generator', views.generator, name='generator'),
    # path('password', views.generator, name='generator'),
]
