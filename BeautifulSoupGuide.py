import requests
from bs4 import BeautifulSoup


#result = requests.get("https://www.lazada.sg/products/cetaphil-gentle-skin-cleanser-1l-i680852034-s2087930187.html?spm=a2o42.seller.list.17.28aa7781iJbMzw&mp=1")
#result = requests.get("https://www.lazada.sg/products/stanley-750ml-stainless-steel-classic-vacuum-flask-water-bottle-25oz-black-for-road-trip-camping-fishing-outdoor-i231388228-s354697774.html?spm=a2o42.searchlist.list.11.64331138fZadw7&search=1")
#result =requests.get("https://www.lazada.sg/products/stanley-cordless-18v-brushless-hammer-drill-driver-sbh201d2k-i698870508-s2175476501.html?spm=a2o42.searchlist.list.11.635a1138ltohLp&search=1")
result = requests.get("https://www.lazada.sg/products/xiaomi-mi-dual-mode-wireless-mouse-silent-edition-i722660567-s2290582957.html?spm=a2o42.searchlist.list.1.10c524e2A2xOuI&search=1")
#result = requests.get("https://www.lazada.sg/products/pre-order-prism-x240-1200r-24-144hz-1ms-curved-fhd-1920-x-1080-freesync-g-sync-ready-gaming-monitor-ships-out-early-to-mid-dec-i225440820-s449843155.html?spm=a2o42.seller.list.1.29b221fayEly84&mp=1")
#result = requests.get("https://www.lazada.sg/products/jaybird-vista-true-wireless-in-ear-earbuds-for-sports-up-to-16-hours-playtime-ipx7-waterproof-and-sweatproof-sport-fit-i1127580252-s4373274206.html?spm=a2o42.searchlist.list.54.489817cfLTkP5T&search=1")
#result = requests.get("https://www.lazada.sg/products/xiaomi-mi-casual-daypack-global-version-lightweight-backpack-i1245518363-s5098572065.html?spm=a2o42.home.flashSale.2.32c046b5u87o3r&search=1&mp=1&c=fs&clickTrackInfo=%7B%22rs%22%3A%220.6666971428571429%22%2C%22prior_score%22%3A%220%22%2C%22submission_discount%22%3A%2275%25%22%2C%22type%22%3A%22entrance%22%2C%22prior_type%22%3A%22MustBuy_itself%22%2C%22userid%22%3A%22%22%2C%22sca%22%3A%2227%22%2C%22hourtonow%22%3A%229%22%2C%22abid%22%3A%22194129%22%2C%22itemid%22%3A%221245518363_0_itself_0.6666971428571429_0.6666971428571429%22%2C%22pvid%22%3A%228e61d1d9-e845-47cf-b8db-764fd63f338c%22%2C%22pos%22%3A%220%22%2C%22rms%22%3A%220.0%22%2C%22c2i%22%3A%220.0%22%2C%22scm%22%3A%221007.17760.194129.%22%2C%22ss%22%3A%220.6666971428571429%22%2C%22i2i%22%3A%220.0%22%2C%22ms%22%3A%220.6666971428571429%22%2C%22itr%22%3A%220.32466666666666666%22%2C%22mt%22%3A%22itself%22%2C%22its%22%3A%221500%22%2C%22promotion_price%22%3A%224.99%22%2C%22anonid%22%3A%22cGHtmRxCoQC9ww8ro6tls53hlv2jqnUE%22%2C%22FinalScore%22%3A%220.0%22%2C%22isc%22%3A%22487%22%2C%22iss2%22%3A%220.9996694179926959%22%2C%22data_type%22%3A%22flashsale%22%2C%22iss1%22%3A%221.0%22%2C%22config%22%3A%22%22%2C%22HP_score%22%3A%220.0%22%2C%22channel_id%22%3A%220000%22%7D&scm=1007.17760.194129.0")
#result = requests.get("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418199.html?spm=a2o42.searchlistcategory.list.8.15793f03DDN6pN&search=1")
#result = request.get("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418196.html?")
#result = requests.get("https://www.lazada.sg/products/xiaomi-redmi-note-8-64gb-4gb-ram-1-year-local-warranty-free-tempered-glass-back-case-i294495557-s5722300854.html?spm=a2o42.searchlistcategory.list.20.15793f03meeHtC&search=1")
#result = requests.get("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418199.html?")

src = result.content
soup = BeautifulSoup(src, 'lxml')
#getName = soup.find("title", ).getText
ogPrice = 29.90
getPercent = soup.find("script", type="text/javascript")

#print(soup)
print(getPercent)

getPercentStr = str(getPercent)

percentValueLocationLast = getPercentStr.find('%', 0)
percentValueLocationFirst = getPercentStr.find('pdt_discount', 0)
if(percentValueLocationLast> 0):
    percentResult = getPercentStr[percentValueLocationFirst + 18:percentValueLocationLast]
    percentResultInt = int(percentResult)
    discountedPrice = ogPrice -(percentResultInt/100)
    print("this is discounted")
    print(discountedPrice)

else:
    print("No discount found")

print(percentResult)
















# this is not the discounted price but the lowest price for the listing
getDiscountedPrice = soup.find("script", type="application/ld+json")
getDiscountedPriceStr = str(getDiscountedPrice)

discountPriceLocationFirst = getDiscountedPriceStr.find('lowPrice' +'"', 0)
firstResultParse =getDiscountedPriceStr[discountPriceLocationFirst +10:]
# first parse to remove redundant "," for discountPriceLocationLast
discountPriceLocationLast = firstResultParse.find(',', 0)
finalResultParse = firstResultParse[:discountPriceLocationLast]
print(finalResultParse)
