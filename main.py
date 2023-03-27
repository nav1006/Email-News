import requests

api = 'fd31f0e33fba47ed8facb678053a6efe'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-02-27&' \
      'sortBy=publishedAt&apiKey=fd31f0e33fba47ed8facb678053a6efe'

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json() #.json() will give dictionary

#Access the article titles and descriptions
for article in content['articles']:
      print(article['title'])
      print(article['description'])