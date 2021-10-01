import pathlib
import main_task
import sys


### This test ensures that the args has been used and gone through successfully ###
def test_enter_arg():
    try:
        main_task.main()
    except:
        SystemExit
    assert len(sys.argv) == 2


### This test makes sure that beautifulsoup has worked throug the url that the user has put through ###
def test_get_content():
    url = "https://www.google.co.uk"
    soup = main_task.get_content(url)
    assert soup


### This test is to check whether a text file has been created from the site given to you by the user ###
def test_print_content():
    main_task.get_content("https://www.google.com")
    main_task.print_content()
    path = pathlib.Path('../this_is_file.txt')
    assert path.exists() == True