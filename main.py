from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse


parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a")
args = parser.parse_args()
url = "https://en.wikipedia.org/wiki/Te_lucis_ante_terminum_(Gardiner)"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


my_file = open("this_is_file.txt","w+")
my_file.write(soup.get_text())

a = args.a

print(soup.get_text())
print(a)
