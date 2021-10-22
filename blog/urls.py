from django.urls import path
from.views import HomeView, PostView, Add_BlogEntry, Edit_BlogEntry, Delete_Entry


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', PostView.as_view(), name='blogpost'),
    path('add-blogentry/', Add_BlogEntry.as_view(), name='add-blogentry'),
    path('article/edit/<int:pk>', Edit_BlogEntry.as_view(), name='edit-blogentry'),
    path('article/<int:pk>/delete', Delete_Entry.as_view(), name='delete-entry'),
]
