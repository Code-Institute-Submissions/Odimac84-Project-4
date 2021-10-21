from django.urls import path
from.views import HomeView, PostView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', PostView.as_view(), name='blogpost'),

]