from django.shortcuts import render
from django.db.models import Q
from posts.models import Post


def home(request):
    query = request.GET.get('query', '').strip()
    query = ' '.join(query.split())

    data = Post.objects.all()

    if query:
        data = data.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        ).distinct()

    return render(request, 'home.html', {'data': data, 'query': query})
