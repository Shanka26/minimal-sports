from django.urls import path
from . import views

urlpatterns = [
    path('', views.getNbaNews),
    path('stories',views.getStories)
]