from django.urls import path
from apps.metrics import views

urlpatterns = [ path('learn',views.learn)]