import requests
from bs4 import BeautifulSoup
import logging


#result = requests.get("https://www.lazada.sg/products/logitech-mx-master-3-advanced-wireless-mouse-with-bluetooth-ultra-fast-magspeed-scroll-in-app-customization-and-pair-up-to-3-devices-work-from-home-home-based-learning-i422836641-s1073562642.html?spm=a2o42.searchlist.list.1.314274deAgHfQj&search=1")
result = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>A Test Webscrape</title>
</head>
<body>
<div class="category1" id="foo">
      <div class="category2" id="bar">
            <div class="category3">
            </div>
            <div class="category4">
                 <div class="category5"> test
                 </div>
            </div>
      </div>
</div>
</body>
</html>
"""
#src = result.content
soup = BeautifulSoup(result, 'lxml')

#print(soup.prettify()) #prints out the entire log

# for a in soup:
#     if(a is not None):
#         getWord = soup.find("div")
#         print(getWord)

getWord = soup.find("div",{"class":"category5"}).getText()
print(getWord)



#for featured_challenge in featured_challenges:
    #print(featured_challenge)
