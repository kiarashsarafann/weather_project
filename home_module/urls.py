from .views import index_page, weather
from django.urls import path

urlpatterns = [
    path('', index_page, name='index_page'),
]
