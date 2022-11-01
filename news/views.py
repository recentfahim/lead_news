from django.views.generic import ListView
from .models import News


class NewsListView(ListView):
    queryset = News.objects.all()[:20]
    context_object_name = 'news_list'
    template_name = 'news_list.html'
