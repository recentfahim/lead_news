from django.core.management.base import BaseCommand, CommandError
from news.models import News
from newsapi import NewsApiClient
import os


class Command(BaseCommand):
    help = 'Fetch millions of articles from over 80,000 large and small news sources and blogs'

    def add_arguments(self, parser):
        parser.add_argument(
            '-s', '--search',
            type=str,
            help='Keywords or a phrase to search for.'
        )
        parser.add_argument(
            '--sources',
            nargs='+',
            type=str,
            help='A comma-seperated string of identifiers for the news sources or blogs'
        )
        parser.add_argument(
            '-c', '--country',
            type=str,
            help='The 2-letter code of the country. e.g "ae", "be", "ca", "au", "fr", "it", "jp", "ru", "us", "ve"'
        )
        parser.add_argument(
            '--category',
            type=str,
            help='A comma-seperated string of category (eg "business", "entertainment", "sports", "technology")'
        )
        parser.add_argument(
            '--page_size',
            type=int,
            help='The number of results to return per page (request). 20 is the default, 100 is the maximum'
        )
        parser.add_argument(
            '-p', '--page',
            type=int,
            help='Use this to page through the results if the total results found is greater than the page size'
        )

    def handle(self, *args, **options):
        news_api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))
        all_articles = news_api.get_top_headlines(
            q=options['search'],
            sources=options['sources'],
            country=options['country'],
            category=options['category'],
            page_size=options['page_size'],
            page=options['page']
        )
        print(all_articles)
        objs = []
        if all_articles.get('status') == 'ok' and all_articles.get('totalResults') > 0:
            articles = all_articles.get('articles')
            for article in articles:
                objs.append(News(
                    source_id=article.get('source').get('id'),
                    source_name=article.get('source').get('name'),
                    author_name=article.get('author'),
                    title=article.get('title'),
                    description=article.get('description'),
                    url=article.get('url'),
                    image_url=article.get('urlToImage'),
                    published_at=article.get('publishedAt'),
                    content=article.get('content')
                ))
            News.objects.bulk_create(objs)
            print('News saved successfully')
        else:
            print("No result or something gone wrong when try to fetch news")
