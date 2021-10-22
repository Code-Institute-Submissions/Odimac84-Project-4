from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class PostView(DetailView):
    model = Post
    template_name = 'blogpost.html'


class Add_BlogEntry(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-blogentry.html'
