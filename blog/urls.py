from django.urls import path
from.views import HomeView, PostView, Add_BlogEntry, Edit_BlogEntry, Delete_Entry, Add_Category, View_By_Category, LikeView, Add_Comment


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostView.as_view(), name='blogpost'),
    path('add-blogentry/', Add_BlogEntry.as_view(), name='add-blogentry'),
    path('add-category/', Add_Category.as_view(), name='add-category'),
    path('article/edit/<int:pk>', Edit_BlogEntry.as_view(), name='edit-blogentry'),
    path('article/<int:pk>/delete', Delete_Entry.as_view(), name='delete-entry'),
    path('category/<str:cats>/', View_By_Category, name='category'),
    path('like/<int:pk>', LikeView, name='post_like'),
    path('article/<int:pk>/comment', Add_Comment.as_view(), name='add-comment'),
]
