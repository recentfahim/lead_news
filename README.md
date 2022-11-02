##  NewsMine with Django and API with Django Rest Framework

News Mine is an web application and also provide API. This application consume news API from [NewsAPI](https://newsapi.org/) which collect news from different news from different sources. This application used NewsAPI python library [newsapi-python](https://github.com/mattlisiv/newsapi-python) to get all the news.

#### Requirements

-   Python 3.9
-   Django 4.1.2
-   Django Rest Framework

#### Install Dependencies

Before installing project dependencies please install `virtualenv` if you don't have it installed your system.

    pip3 install virtualenv
 
Create a virtual environment using `virtualenv`

    virtualenv venv

Activate the virtual environment `venv`

    source venv/bin/activate

Install all dependency from  root  folder

    pip install -r requirements.txt

#### Database Setup

You can use any database you want, but in this project MySQL has been used.

Once a database is created and connected, migrate the models

    python manage.py makemigrations
And then

    python manage.py migrate

Create and configure the  `.env`  file. Put all essential configuration in this file, like Secret, Database credentials, Allowed hosts, etc.

Now, run the project with
python manage.py runserver

Open the browser and put `127.0.0.1:8000` to see the application output.

Create a superuser to get access to admin

    python manage.py createsuperuser

You can see the Django admin panel at `127.0.0.1:8000/admin`.

Check the `urls.py` inside `lead_news` folder and navigate to the urls to view the web and API outputs.

#### Management Commands

To consume news from [/v2/everything](https://newsapi.org/docs/endpoints/everything) run the management commands `fetch_everything.py` 

    python manage.py fetch_everything

Example of using params,

    python manage.py fetch_everything -s "search string" --sort_by popularity

There are multiple optional parameters given below,

| Params | Params short | Description |
|--|--|--|  
| `--search` | `-s` | Keywords or phrases to search for in the article title and body. |  
| `--sources` | - | A comma-seperated string of identifiers (maximum 20) for the news sources or blogs you want headlines from. |  
| `--language` | `-l` | The 2-letter ISO-639-1 code of the language you want to get headlines for. Possible options: `ar` `de` `en` `es` `fr` `he` `it` `nl` `no` `pt` `ru` `sv` `ud` `zh`. |  
| `--domains` | `-d` | A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to restrict the search to. |  
| `--from_date` | `-f` | A date and optional time for the _oldest_ article allowed. This should be in ISO 8601 format (e.g. `2022-11-02` or `2022-11-02T19:52:30`) |  
| `--to_date` | `-t` | A date and optional time for the _newest_ article allowed. This should be in ISO 8601 format (e.g. `2022-11-02` or `2022-11-02T19:52:30`) |  
| `--sort_by` | - | The order to sort the articles in. Possible options: `relevancy`, `popularity`, `publishedAt`. <br> `relevancy` = articles more closely related to `q` come first. <br> `popularity` = articles from popular sources and publishers come first.  <br>`publishedAt` = newest articles come first. |  
| `--page_size` | - | The number of results to return per page. |  
| `--page` | `-p` | Use this to page through the results. |
 
 
To consume news from [/v2/top-headlines](https://newsapi.org/docs/endpoints/top-headlines) run the management commands `fetch_top_headlines.py` 

    python manage.py fetch_top_headlines

Example of using params,

    python manage.py fetch_top_headlines -s "search string" --category technology

There are multiple optional parameters given below,

| Params | Params short | Description |
|--|--|--|  
| `--search` | `-s` | Keywords or phrases to search for in the article title and body. |  
| `--sources` | - | A comma-seperated string of identifiers (maximum 20) for the news sources or blogs you want headlines from. |  
| `--category` | - | The category you want to get headlines for. Possible options: `business` `entertainment` `general` `health` `science` `sports` `technology` |  
| `--country` | `-c` | The 2-letter ISO 3166-1 code of the country you want to get headlines for. |  
| `--page_size` | - | The number of results to return per page. |  
| `--page` | `-p` | Use this to page through the results. |
 
*In the table `-` means there is no short form for the respective params.*