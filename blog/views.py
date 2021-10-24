from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostEntry, EditEntry
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_date']

    def get_context_data(self, *args, **kwargs):
        meny = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["meny"] = meny
        return context


class PostView(DetailView):
    model = Post
    template_name = 'blogpost.html'

    def get_context_data(self, *args, **kwargs):
        meny = Category.objects.all()
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context["meny"] = meny
        return context


class Add_BlogEntry(CreateView):
    model = Post
    form_class = PostEntry
    template_name = 'add-blogentry.html'


class Add_Category(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'


class Edit_BlogEntry(UpdateView):
    model= Post
    form_class = EditEntry
    template_name = 'edit-blogentry.html'


class Delete_Entry(DeleteView):
    model = Post
    template_name = 'delete-entry.html'
    success_url = reverse_lazy('home')


def View_By_Category(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
