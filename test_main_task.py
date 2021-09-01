import pathlib
import main_task
import sys


def test_enter_arg():
    try:
        main_task.main()
    except:
        SystemExit
    assert len(sys.argv) == 2


def test_get_content():
    url = "https://www.google.co.uk"
    soup = main_task.get_content(url)
    assert soup


def test_print_content():
    main_task.get_content("https://www.google.com")
    main_task.print_content()
    path = pathlib.Path('this_is_file.txt')
    assert path.exists() == True