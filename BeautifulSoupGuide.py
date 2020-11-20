import requests
from bs4 import BeautifulSoup


#result = requests.get("https://www.lazada.sg/products/cetaphil-gentle-skin-cleanser-1l-i680852034-s2087930187.html?spm=a2o42.seller.list.17.28aa7781iJbMzw&mp=1")
result = requests.get("https://www.lazada.sg/products/stanley-750ml-stainless-steel-classic-vacuum-flask-water-bottle-25oz-black-for-road-trip-camping-fishing-outdoor-i231388228-s354697774.html?spm=a2o42.searchlist.list.11.64331138fZadw7&search=1")
#result =requests.get("https://www.lazada.sg/products/stanley-cordless-18v-brushless-hammer-drill-driver-sbh201d2k-i698870508-s2175476501.html?spm=a2o42.searchlist.list.11.635a1138ltohLp&search=1")
src = result.content
soup = BeautifulSoup(src, 'lxml')
getName = soup.find("title", ).getText
print(getName)
getNameStr =str(getName)


nameLocationLast = getNameStr.find("|", 0)
nameLocationFirst = getNameStr.find(">", 0)

nameResult = getNameStr[nameLocationFirst +1:nameLocationLast]

print(nameResult)
print(len(nameResult))



#print(soup.prettify())