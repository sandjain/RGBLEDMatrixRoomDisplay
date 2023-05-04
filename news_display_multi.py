import requests

def fetch_news(api_key, keyword, language='en'):
    # Define the endpoint
    url = 'https://newsapi.org/v2/everything?'

    # Specify the query and number of returns
    parameters = {
        'q': keyword, # query phrase
        'pageSize': 20,  # maximum is 100
        'apiKey': api_key, # your own API key
        'language': language # language of the news
    }

    # Make the request
    response = requests.get(url, params=parameters)

    # Convert the response to JSON format and pretty print it
    response_json = response.json()

    for news in response_json['articles']:
        print(f"Title : {news['title']}")
        print(f"Description : {news['description']}")
        print(f"URL: {news['url']}")
        print('---'*20)

# Use the function
api_key = 'your_api_key_here'  # replace this with your API key
keyword = 'Artificial Intelligence'
fetch_news(api_key, keyword)



$ pip install newsapi-python
Usage
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='YOUR KEY GOES HERE')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()