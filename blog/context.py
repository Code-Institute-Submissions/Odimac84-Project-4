from django.conf import settings
from blog.models import Category


def get_meny_context(self, *args, **kwargs):
    meny = Category.objects.all()
    context = {
        'meny': meny,
    }
    return context
