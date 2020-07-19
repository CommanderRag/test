import os
import re
import sys
import time
import requests

from bs4 import BeautifulSoup

print("working")
number=variables['number']
print(number)
url = "https://4anime.to/boruto-naruto-next-generations-episode-{}".format(number)
r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
text = soup.find_all(text=True)
output = ""
blacklist = [
    '[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script'
]
for t in text:
    if t.parent.name not in blacklist:
        output += '{}'.format(t)

if(output.find("Episode {}".format(number)))==-1:
  message="Episode {} is not out yet!".format(number)
  response = requests.post('https://notify.run/4S9uUexUL6gEhHZu', data=message)

  
  
else:
  message="Episode {} is out now!".format(number)
  response = requests.post('https://notify.run/4S9uUexUL6gEhHZu', data=message)
