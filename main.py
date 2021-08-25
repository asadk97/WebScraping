from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse
import urllib

parser = argparse.ArgumentParser(description='Enter the website you would like to be scraped')
parser.add_argument("--site", default=0, type=str, help='Type in the site: ')
args = parser.parse_args()


url = (args.site)
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


my_file = open("this_is_file.txt","w+")
my_file.write(soup.get_text())

print(soup.get_text())
