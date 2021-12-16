from bs4 import BeautifulSoup
import os

base = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(base, 'ejemplo.html'))
print(html)
soup = BeautifulSoup(html, 'html.parser')
print(soup)


