from django.urls import path
from . import views

urlpatterns = [
    path('', views.getNbaNews),
    path('stories/nba',views.getStories),
    path('stories/nba/<str:team>',views.getNbaTeam)
]