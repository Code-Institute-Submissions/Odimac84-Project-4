from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostEntry, EditEntry


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class PostView(DetailView):
    model = Post
    template_name = 'blogpost.html'


class Add_BlogEntry(CreateView):
    model = Post
    form_class = PostEntry
    template_name = 'add-blogentry.html'

class Edit_BlogEntry(UpdateView):
    model= Post
    form_class = EditEntry
    template_name = 'edit-blogentry.html'
