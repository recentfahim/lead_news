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
            help='Keywords or phrases to search for in the article title and body'
        )
        parser.add_argument(
            '--sources',
            nargs='+',
            type=str,
            help='A comma-seperated string of identifiers for the news sources or blogs'
        )
        parser.add_argument(
            '-l', '--language',
            type=str,
            help='The 2-letter code of the language. e.g "ar", "de", "en", "es", "fr", "it", "pt", "ru", "sv", "zh"'
        )
        parser.add_argument(
            '-d', '--domains',
            nargs='+',
            type=str,
            help='A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com) to restrict the search to.'
        )
        parser.add_argument(
            '-f', '--from_date',
            type=str,
            help='A date and optional time for the oldest article allowed. Format "2022-11-01" or "2022-11-01T16:52:21"'
        )
        parser.add_argument(
            '-t', '--to_date',
            type=str,
            help='A date and optional time for the newest article allowed. Format "2022-11-01" or "2022-11-01T16:52:21"'
        )
        parser.add_argument(
            '--sort_by',
            type=str,
            help='The order to sort the articles in. Possible options: "relevancy", "popularity", "publishedAt"'
        )
        parser.add_argument(
            '--page_size',
            type=int,
            help='The number of results to return per page'
        )
        parser.add_argument(
            '-p', '--page',
            type=int,
            help='Use this to page through the results'
        )

    def handle(self, *args, **options):
        news_api = NewsApiClient(api_key=os.getenv('NEWS_API_KEY'))

        all_articles = news_api.get_everything(
            q=options['search'],
            sources=','.join(options['sources']),
            domains=','.join(options['domains']),
            from_param=options['from_date'],
            to=options['to_date'],
            language=options['language'],
            sort_by=options['sort_by'],
            page_size=options['page_size'],
            page=options['page']
        )
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
