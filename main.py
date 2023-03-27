import requests
import send_email

api = 'fd31f0e33fba47ed8facb678053a6efe'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-02-27&' \
      'sortBy=publishedAt&apiKey=fd31f0e33fba47ed8facb678053a6efe'

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json() #.json() will give dictionary

#Access the article titles and descriptions
body = ''
for article in content['articles']:
      if article['title'] is not None:
            body = body + article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode('utf-8')
send_email.send_email(message=body)