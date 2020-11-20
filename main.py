import requests
from bs4 import BeautifulSoup
from database import *
import string

alphabetList = list(string.ascii_uppercase)
productUrlList = []


productUrlList.append("https://www.lazada.sg/products/stanley-750ml-stainless-steel-classic-vacuum-flask-water-bottle-25oz-black-for-road-trip-camping-fishing-outdoor-i231388228-s354697774.html?spm=a2o42.searchlist.list.11.64331138fZadw7&search=1")
productUrlList.append("https://www.lazada.sg/products/logitech-mx-master-3-advanced-wireless-mouse-with-bluetooth-ultra-fast-magspeed-scroll-in-app-customization-and-pair-up-to-3-devices-work-from-home-home-based-learning-i422836641-s1073562642.html?spm=a2o42.searchlist.list.1.314274deAgHfQj&search=1")
productUrlList.append("https://www.lazada.sg/products/cetaphil-gentle-skin-cleanser-1l-i680852034-s2087930187.html?spm=a2o42.seller.list.17.28aa7781iJbMzw&mp=1")
productUrlList.append("https://www.lazada.sg/products/sandisk-ultra-sd-uhs-i-u1-up-to-80mbs-read-memory-card-sdsdunr-32gb-64gb-128gb-256gb-i487314372-s1333002832.html?spm=a2o42.seller.list.45.304f7eefzf9Crk&mp=1")
productUrlList.append("https://www.lazada.sg/products/stanley-cordless-18v-brushless-hammer-drill-driver-sbh201d2k-i698870508-s2175476501.html?spm=a2o42.searchlist.list.11.635a1138ltohLp&search=1")
productUrlList.append("https://www.lazada.sg/products/xiaomi-mi-dual-mode-wireless-mouse-silent-edition-i722660567-s2290582957.html?spm=a2o42.searchlist.list.1.10c524e2A2xOuI&search=1")
productUrlList.append("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418199.html?")
productUrlList.append("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418196.html?")
productUrlList.append("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418199.html?")  # Iphone SE White 256GB

initialCellBlock = -1

for product in productUrlList:
    result = requests.get(product)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    getPrice = soup.find("script", type="text/javascript").getText  # get the script that has the price tag in it
    getPriceStr = str(getPrice)
    priceLocation = getPriceStr.find("$", 0)
    priceResult = getPriceStr[priceLocation:priceLocation+6]
    # getPrice only retrieve the original price



 
    getName = soup.find("title", ).getText  # get the script that has the title in it
    getNameStr = str(getName)
    nameLocationLast = getNameStr.find("|", 0)
    nameLocationFirst = getNameStr.find(">", 0)
    nameResult = getNameStr[nameLocationFirst + 1:nameLocationLast]

    initialCellBlock += 1
    cellBlockResult = alphabetList[initialCellBlock]  # output Strings

    #print("Below is supposed to show price")
    #print(cellBlockResult)
    #print(type(cellBlockResult))

    writeHeaderProduct(nameResult, cellBlockResult)
    writeWorkBook(priceResult, cellBlockResult)




