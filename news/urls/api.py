from django.urls import path
from news.views import NewsAPIView


urlpatterns = [
    path('news/', NewsAPIView.as_view(), name='news_list_api'),
]
