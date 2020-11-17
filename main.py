import requests
from bs4 import BeautifulSoup


productUrlList = []


productUrlList.append("https://www.lazada.sg/products/stanley-750ml-stainless-steel-classic-vacuum-flask-water-bottle-25oz-black-for-road-trip-camping-fishing-outdoor-i231388228-s354697774.html?spm=a2o42.searchlist.list.11.64331138fZadw7&search=1")
productUrlList.append("https://www.lazada.sg/products/logitech-mx-master-3-advanced-wireless-mouse-with-bluetooth-ultra-fast-magspeed-scroll-in-app-customization-and-pair-up-to-3-devices-work-from-home-home-based-learning-i422836641-s1073562642.html?spm=a2o42.searchlist.list.1.314274deAgHfQj&search=1")
productUrlList.append("https://www.lazada.sg/products/cetaphil-gentle-skin-cleanser-1l-i680852034-s2087930187.html?spm=a2o42.seller.list.17.28aa7781iJbMzw&mp=1")

for product in productUrlList:
    result = requests.get(product)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    getPrice = soup.find("script", type="text/javascript").getText  # get the script that has the price tag in it
    getPriceStr = str(getPrice)
    priceLocation = getPriceStr.find("$", 0)

    print("Below is supposed to show price")
    print(getPriceStr[priceLocation:priceLocation+6])




