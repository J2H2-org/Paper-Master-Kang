from django.http import JsonResponse
from django.core.cache import cache

from .models import Post


def my_view(request):
    posts = cache.get_or_set('posts', Post.objects.all().values('id', 'text'))
    return JsonResponse(list(posts), safe=False)
