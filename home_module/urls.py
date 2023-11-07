from .views import IndexPageView
from django.urls import path

urlpatterns = [
    path('', IndexPageView.as_view(), name='index_page')
]
