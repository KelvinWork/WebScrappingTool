from selenium import webdriver
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get("https://www.lazada.sg/products/logitech-mx-master-3-advanced-wireless-mouse-with-bluetooth-ultra-fast-magspeed-scroll-in-app-customization-and-pair-up-to-3-devices-work-from-home-home-based-learning-i422836641-s1073562642.html?spm=a2o42.searchlist.list.1.314274deAgHfQj&search=1")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
productPrice = driver.find_element_by_class_name('pdp-product-price').text

print(productPrice)
assert "No results found." not in driver.page_source
#driver.close()