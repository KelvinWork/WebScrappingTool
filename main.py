import requests
from bs4 import BeautifulSoup
from database import *
import string
import datetime
import random
import time
start_time = time.time()

# second alternative to extract data
from selenium import webdriver

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)


alphabetList = list(string.ascii_uppercase)
productUrlList = []

myUserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Dnt": "1",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": myUserAgent,
  }

lazHeader = {
    "authority" : "www.lazada.sg",
    "method": "GET",
    "path": "/",
    "scheme": "https",
    "accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "lzd_cid=34ab3bed-0271-432d-bce8-029ca336431d; t_fv=1604747055002; t_uid=XOgZkfZxnkWTAt8EbTNYnHmWrJ6uKJ6l; cna=Lm0tGGmV9k8CAdtLV0Lt+ege; _lang=en_US; anon_uid=50040b7a73eb19ec22500b06548c9313; userLanguageML=en; _gcl_au=1.1.733531553.1604747062; _fbp=fb.1.1604747063424.1363167982; _ga=GA1.2.302084276.1604747236; _bl_uid=g3knUhqs719lzz37agdvd01umtpy; miidlaz=miid5odksc1en586hc4h8h; lzd_click_id=clk5odksc1en586hc0h8g; hng=SG|en|SGD|702; _fbc=fb.1.1605956736072.IwAR3DwsMY0O_kVwvVamLklU7ePg16GqCRsPEySnTwWs9Ea7DI9UAILgOQDSk; _gcl_aw=GCL.1605959588.Cj0KCQiAkuP9BRCkARIsAKGLE8XrbOaEbdv1yczKcEzLggTAs3VFrvouaRh2J6Z6wubGRbQvytToB3EaAvfkEALw_wcB; _gid=GA1.2.959720024.1605959588; _gac_UA-49088239-1=1.1605959588.Cj0KCQiAkuP9BRCkARIsAKGLE8XrbOaEbdv1yczKcEzLggTAs3VFrvouaRh2J6Z6wubGRbQvytToB3EaAvfkEALw_wcB; lzd_sid=1b547c8641799c6331a0118258313cf8; _m_h5_tk=67c330583d57f4b6a8cc8b99cb226665_1606030154697; _m_h5_tk_enc=b8619203cb0030dc2d65f3363455927d; _tb_token_=eb35b5e5a975e; xlly_s=1; JSESSIONID=DBA16D4689F728C63D1FAC19E18D84EE; XSRF-TOKEN=b3ced22a-6185-4dad-b4e1-6b1128d05b22; t_sid=8p8EruQV32LmBCkW6BJro1raIVuECaul; utm_channel=NA; _uetsid=ddc1d2002b2711ebabff4979733405b4; _uetvid=fe1ccd1020e811eba5b2e93dca57506c; isg=BGxsudbwH4XJrAulCao3N51dPUqeJRDPTXfOysaud5e60Qzb7jUKX2Ig8ZHp2Ugn; l=eBP7dqLuO6BAJugpBO5anurza77OmQOb4sPzaNbMiInca1SO9F9w8NQV7Z69Wdtj_tCEletr09hQ7RLHR3fRwxDDBtT4DfCofxvO.; tfstk=ce_NBuw55PUwFGYb2FTqf3MnQ_8OZ_1Gi2RWjir7VcCtAGtGiHMvtQgpTI98-hf..",
    "if-none-match": 'W/"b6c99-FCZDyiu70qZuaEJ/qwmZxcv/E6Y"',
    "referer": "https://www.lazada.sg/",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",}


#r = requests.get('example.com',headers=headers,proxies={'https': proxy_url})

productUrlList.append("https://www.lazada.sg/products/stanley-750ml-stainless-steel-classic-vacuum-flask-water-bottle-25oz-black-for-road-trip-camping-fishing-outdoor-i231388228-s354697774.html?spm=a2o42.searchlist.list.11.64331138fZadw7&search=1")
productUrlList.append("https://www.lazada.sg/products/logitech-mx-master-3-advanced-wireless-mouse-with-bluetooth-ultra-fast-magspeed-scroll-in-app-customization-and-pair-up-to-3-devices-work-from-home-home-based-learning-i422836641-s1073562642.html?spm=a2o42.searchlist.list.1.314274deAgHfQj&search=1")
productUrlList.append("https://www.lazada.sg/products/cetaphil-gentle-skin-cleanser-1l-i680852034-s2087930187.html?spm=a2o42.seller.list.17.28aa7781iJbMzw&mp=1")
productUrlList.append("https://www.lazada.sg/products/sandisk-ultra-sd-uhs-i-u1-up-to-80mbs-read-memory-card-sdsdunr-32gb-64gb-128gb-256gb-i487314372-s1333002832.html?spm=a2o42.seller.list.45.304f7eefzf9Crk&mp=1")
productUrlList.append("https://www.lazada.sg/products/stanley-cordless-18v-brushless-hammer-drill-driver-sbh201d2k-i698870508-s2175476501.html?spm=a2o42.searchlist.list.11.635a1138ltohLp&search=1")
productUrlList.append("https://www.lazada.sg/products/xiaomi-mi-dual-mode-wireless-mouse-silent-edition-i722660567-s2290582957.html?spm=a2o42.searchlist.list.1.10c524e2A2xOuI&search=1")
productUrlList.append("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418199.html?")
productUrlList.append("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418196.html?")
productUrlList.append("https://www.lazada.sg/products/apple-iphone-se-i672058450-s2050418199.html?")  # Iphone SE White 256GB
productUrlList.append("https://www.lazada.sg/products/prism-x240-1200r-24-144hz-1ms-curved-fhd-1920-x-1080-freesync-g-sync-ready-gaming-monitor-i225440820-s449843155.html?spm=a2o42.searchlist.list.1.99ed1b21etK8ej&search=1")

initialCellBlock = 0

for product in productUrlList:
    loop_time = time.time()
    driver.get(product)
    productPrice = driver.find_element_by_class_name('pdp-product-price').text

    productPriceStr = str(productPrice)
    currentProductPriceFirst = productPriceStr.find("$", 0)
    currentProductPriceLast = productPriceStr.find(".", 0)
    currentPrice = productPriceStr[currentProductPriceFirst + 0: currentProductPriceLast + 3]  # get the current pricing on the listing


    originalPriceFirst = productPriceStr.find("$", 2)
    originalPriceLast = productPriceStr.find(".", currentProductPriceLast + 1)
    originalPrice = productPriceStr[originalPriceFirst + 0:originalPriceLast + 3]   # get the original pricing on the listing

    result = requests.get(product, headers=lazHeader)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    # initial method of getting the pricing on the listing
    getPrice = soup.find("script", type="text/javascript").getText  # get the script that has the price tag in it
    getPriceStr = str(getPrice)
    priceLocation = getPriceStr.find("$", 0)
    priceResult = getPriceStr[priceLocation:priceLocation+6]  # getPrice only retrieve the original price



    getName = soup.find("title", ).getText   # get the script that has the title in it
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
    writeWorkBook(currentPrice, cellBlockResult)
    print("Product {} extraction completed".format(initialCellBlock))
    print("\n")
    print("Extraction Finished in  {:2f} seconds ---"  .format(time.time() - loop_time))

writeDateExtracted()
print("Programme Finished in  {:2f} seconds ---"  .format(time.time() - start_time))


