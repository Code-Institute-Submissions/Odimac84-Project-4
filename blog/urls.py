from django.urls import path
from.views import HomeView, PostView, Add_BlogEntry


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', PostView.as_view(), name='blogpost'),
    path('add-blogentry/', Add_BlogEntry.as_view(), name='add-blogentry'),
]
