import pathlib
import main_task


def test_url():
    test = main_task.TextExtractor("www.google.co.uk")
    url = test.url_test()
    assert "https://" in url

