from django import forms
from .models import Post, Category, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# Code for the category choices
choices = Category.objects.all().values_list('category_name', 'category_name')

category_list = []

for item in choices:
    category_list.append(item)


class PostEntry(forms.ModelForm):
    # the form for making a blogpost
    class Meta:
        model = Post
        fields = (
            'title', 'title_tag', 'author', 'category', 'blog_image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '', 'id':
                'author-id',
                'type': 'hidden'
                }),
            'category': forms.Select(choices=category_list, attrs={
                'class': 'form-control'
                }),
            'body': SummernoteWidget(),
        }


class EditEntry(forms.ModelForm):
    # form for editing a blogpost
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'blog_image', 'body', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=category_list, attrs={
                'class': 'form-control'
                }),
            'body': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    # form to make a comment on a blogpost
    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
