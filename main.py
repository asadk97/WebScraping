from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse
import urllib

#This allows the user to type in the site when they enter in the terminal
parser = argparse.ArgumentParser(description='Enter the website you would like to be scraped')
parser.add_argument("--site", default=0, type=str, help='Type in the site: ')
args = parser.parse_args()

#Where the BS takes in the url data and html code
url = (args.site)
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#Creates a text file from the site
my_file = open("this_is_file.txt","w+")
my_file.write(soup.get_text())

#Prints out results
print(soup.get_text())
