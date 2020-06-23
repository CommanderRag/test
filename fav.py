import os
import re
import sys
import time
import requests

from bs4 import BeautifulSoup
from notify_run import Notify

notify = Notify()
print(notify.register())
time.sleep(50)
sleep=86400
print("working")

url = "https://4anime.to/boruto-naruto-next-generations-episode-155?id=33531"
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

while output.find("Episode 155") == -1:
    notify.send("Episode 155 is not out yet!")
    print("executed script")
    
    time.sleep(sleep)
    sleep=sleep-18000
    if sleep<=10800:
        sleep=10800
    url = "https://4anime.to/boruto-naruto-next-generations-episode-155?id=33531"
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
else:
    notify.send("Episode 155 is out now!")
    sys.exit()

