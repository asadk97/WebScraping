from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse
import pytest


def get_content(argurl):
    # Where BeautifulSoup takes in the url data and html code
    url = (argurl)
    page = urlopen(url)
    html = page.read().decode("utf-8", errors='ignore')
    soup = BeautifulSoup(html, "html.parser")
    return soup


def main():
    # This is where the user will type in the site when they enter in the terminal
    parser = argparse.ArgumentParser(description='Enter the website you would like to be scraped')
    parser.add_argument("--site", default=0, type=str, help='Type in the site: ')
    parser.parse_args()
    args = parser.parse_args()
    ed = args.site

    soup = get_content(args.site)

    # Creates a text file from the site
    my_file = open("this_is_file.txt", "w+")
    my_file.write(soup.get_text())

    # Prints out results
    print(soup.get_text())


if __name__ == "__main__":
    main()
