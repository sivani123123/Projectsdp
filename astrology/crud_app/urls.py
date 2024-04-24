# crud_app/urls.py
from django.urls import path
from .views import prediction_list

urlpatterns = [
    path('predictions/', prediction_list, name='prediction_list'),

]
