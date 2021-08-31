import pathlib
import main_task


def test_url():
    test = main_task.url("www.google.co.uk")
    url = test.main()
    assert "https://" in url

