from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('make_prediction/', make_prediction, name='make_prediction')
]
