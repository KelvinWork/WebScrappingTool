import requests
from bs4 import BeautifulSoup
from BeautifulSoupGuide import *
import string


alphabetList = list(string.ascii_uppercase)

urlTest = ["First List", "Second List", "Third List"]

blockPlacement = -1

print(alphabetList[1])

for x in urlTest:

    blockPlacement += 1
    getTwoArugmentTest(x, alphabetList[blockPlacement])