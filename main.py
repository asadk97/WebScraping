from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Te_lucis_ante_terminum_(Gardiner)"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
my_file = open("this_is_file.txt","w+")
my_file.write(soup.get_text())
print(soup.get_text())