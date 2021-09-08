# WebScraping with Unit Test and command lines



### Description

A simple web scraping code that takes the data from a website of your choice that you enter in yourself, personally I would recommend to copy and paste the website directly into the terminal. It works by the url entered going through the code and then the code would read through the html coding of the page and then take out any unnecessary data such as tags. 

The code also does not allow any sites without the https:// before it. The unit test would then fail if not included

This part also contains a flask coded html page where the user can input the site they would like and for the web scrape to go through from there


### Tutorial and Instructions

To run the web scraping simply enter in the terminal:

1. `$python main_task.py --site` 
2. Add in the site that you would like to scrape after `$python main_task.py --site "https://www.google.co.uk`



This branch also contains both the command lines and the unit tests to ensure that the user is able to input the correct site formats



### Tutorial for running Flask development 

To run the flask part of the code you would have to first enter in the terminal:

1. If you are using windows or linux it would be `$ set FLASK_APP=app.py` or if you are using macOS `export FLASK_APP=app.py`
2. Same thing for which one you are using so for windows or linux `$ set FLASK_ENV=development` and for macOS `export FLASK_ENV=development`
3. `flask run`
4. You will get a link then in the terminal simply copy and paste that onto any browser and you will then see it run in for testing
