from django.views.generic import ListView
from .models import News
from rest_framework import generics
from .serializers import NewsSerializer
from .generics import NewsPagination


class NewsListView(ListView):
    queryset = News.objects.all()
    paginate_by = 20
    context_object_name = 'news_list'
    template_name = 'home.html'


class NewsAPIView(generics.ListAPIView):
    model = News
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
