import requests
from bs4 import BeautifulSoup
import logging



result2 = requests.get("https://www.lazada.sg/products/stanley-750ml-stainless-steel-classic-vacuum-flask-water-bottle-25oz-black-for-road-trip-camping-fishing-outdoor-i231388228-s354697774.html?spm=a2o42.searchlist.list.11.64331138fZadw7&search=1")
result = requests.get("https://www.lazada.sg/products/logitech-mx-master-3-advanced-wireless-mouse-with-bluetooth-ultra-fast-magspeed-scroll-in-app-customization-and-pair-up-to-3-devices-work-from-home-home-based-learning-i422836641-s1073562642.html?spm=a2o42.searchlist.list.1.314274deAgHfQj&search=1")
src = result2.content
soup = BeautifulSoup(src, 'lxml')

#print(soup.prettify())
getPrice = soup.find("script", type ="text/javascript").getText
#extractPrice = getPrice

print(getPrice)
print("Blanks")
print(type(getPrice))
getPriceStr = str(getPrice)
priceLocation = getPriceStr.find("$", 0)

print("Below is supposed to show price")
print(getPriceStr[priceLocation:priceLocation+6])

print(type(getPriceStr))
print(priceLocation)

#print(extractPrice)

