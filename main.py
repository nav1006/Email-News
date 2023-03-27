import requests
import send_email

api = 'fd31f0e33fba47ed8facb678053a6efe'
topic = 'tesla'
url = f'https://newsapi.org/v2/everything?q={topic}&from=2023-02-27&' \
      'sortBy=publishedAt&apiKey=fd31f0e33fba47ed8facb678053a6efe' \
      '&language=en'

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json() #.json() will give dictionary

#Access the article titles and descriptions
body = ''
for article in content['articles'][:20]:
      if article['title'] is not None:
            body = f"Subject: Today's news: {topic}" \
                   + '\n' +body + article['title'] + '\n' \
                   + article['description'] \
                   +'\n' + article['url'] + 2*'\n'

body = body.encode('utf-8')
send_email.send_email(message=body)