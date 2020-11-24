from django.urls import path, include

from . import views


app_name = 'Landing'

urlpatterns = [
      path('', views.contect, name="FrutoPedia"),
    
]