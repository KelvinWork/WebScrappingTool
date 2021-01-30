from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get("URL")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
productPrice = driver.find_element_by_class_name('pdp-product-price').text
category = driver.find_elements_by_class_name('pdp-block module')
productPriceStr = str(productPrice)
productPriceFirst = productPriceStr.find("$", 0)
productPriceLast = productPriceStr.find(".", 0)
lowPrice = productPriceStr[productPriceFirst + 0: productPriceLast + 3]

originalPriceFirst = productPriceStr.find("$", 2)
originalPriceLast = productPriceStr.find(".", productPriceLast + 1)
originalPrice = productPriceStr[originalPriceFirst + 0:originalPriceLast + 3]

# test = re.findall('$', productPriceStr)
# print(test)
for value in category:
    print(value.text)
print(originalPrice)
print("------------")
print(lowPrice)
print("------------")
print(productPrice)
if '\n' in productPriceStr:
    print("There is new line")
assert "No results found." not in driver.page_source
#driver.close()