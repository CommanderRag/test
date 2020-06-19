import os
import re
#import urlextract
import sys
import time
import requests

from bs4 import BeautifulSoup
from notify_run import Notify


notify=Notify()
print(notify.register())
time.sleep(25)

print("working")

url="https://4anime.to/boruto-naruto-next-generations-episode-155?id=33531"
r=requests.get(url)
html=r.content
soup=BeautifulSoup(html,'html.parser')
text=soup.find_all(text=True)
output="" 
blacklist=[
          '[document]','noscript','header','html','meta','head','input','script'
          ]
for t in text:
        if t.parent.name not in blacklist:
         output+='{}'.format(t)

 
if(output.find("Episode 155")!=-1):
       notify.send("Episode 155 is out now!")
       sys.exit()

else:
       notify.send("Episode 155 is not out yet!")
       print("executed script")
       date_time = time.strftime("%b %d %Y %-I:%M %p")
       print(date_time)
       time.sleep(86400)
       os.execl(sys.executable, sys.executable, * sys.argv)
       
