import requests
import openapi_client
from pprint import pprint
from com.worldnewsapi import news_api


configuration = openapi_client.Configuration(
    host = "https://api.worldnewsapi.com"
)

configuration.api_key['apiKey'] = 

with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = news_api.NewsApi(api_client)
url = "https://www.bbc.com/news/world-us-canada-59340789" # str | The url of the news.
analyze = True # bool | Whether to analyze the news (extract entities etc.) (default to False)

try:
    # Extract News
    api_response = api_instance.extract_news(url, analyze)
    pprint(api_response)
except openapi_client.ApiException as e:
    print("Exception when calling NewsApi->extract_news: %s\n" % e)
    

#parameters = {
 #   "text": ['Presidente', 'AMLO', 'Andres Manuel Lopez Obrador'],
  #  'source-countries': 'mx',
   # 'min-sentiment': -0.5,
   # 'max-sentiment': 0.5,
   # 'earliest-publish-date': '2023-09-14',
   # 'new-sources': 'https://elpais.com/noticias/mexico/, https://www.milenio.com/, https://www.unotv.com/, https://www.eluniversal.com.mx/, https://cnnespanol.cnn.com/, https://www.jornada.com.mx/',
   # 'entities': 'LOC:mexico',
   # 'sort': 'sentiment',
   # 'sort-direction': 'ASC'
   # }
    
try:
    # Search News
    api_response = api_instance.search_news(
    text='estudiantil',
    source_countries='mx',
    language='es',
    )
    pprint(api_response)
except openapi_client.ApiException as e:
    print("Exception when calling NewsApi->search_news: %s\n" % e)

#response = requests.get("https://api.worldnewsapi.com/search-news?text=tesla")
#print(response.status_code) # prints the status code of the response
#print(response.json()) # prints the JSON response
#GET https://api.worldnewsapi.com/search-news?text=tesla 