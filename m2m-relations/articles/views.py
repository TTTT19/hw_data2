from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Article_Tag


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    object_list_2 = Article_Tag.objects.all()
    context = {'object_list':object_list, 'object_list_2': object_list_2}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
