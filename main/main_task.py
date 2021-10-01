from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse


def get_content(argurl):
    # Where BeautifulSoup takes in the url data and html code
    url = argurl
    page = urlopen(url)
    html = page.read().decode("utf-8", errors='ignore')
    global soup
    soup = BeautifulSoup(html, "html.parser")
    return soup.text


def enter_arg():
    # This is where the user will type in the site when they enter in the terminal

    parser = argparse.ArgumentParser(description='Enter the website you would like to scrape')
    parser.add_argument("--site", default=0, type=str, help='Type in the site: ')
    args = parser.parse_args()
    return args


def print_content():
    # Creates a text file from the site
    my_file = open("../this_is_file.txt", "w+")
    my_file.write(soup.get_text())

    print(soup.get_text())


def main():
    args = enter_arg()
    get_content(args.site)
    print_content()


if __name__ == "__main__":
    main()
