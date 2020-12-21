
from movie_selector_current import Entertainment
import unittest
import youtube
import imdb
import ott


def test_platform():
    """This method will test the main script"""
    my_entertainment = Entertainment()
    assert my_entertainment.platform == None
    assert my_entertainment.result == None

def test_youtube():
    """This method will test the youtube script. First run the youtube script, then copy
       and paste the results in the assert statement below. Finally run this test script. If 
       successful, the message "Everything Passed" will be printed.
    """
    assert youtube.lookup_youtube("peppermint")[0] == "Peppermint Trailer #1 (2018) | Movieclips Trailers"

def imdb_id():
    """This method will test the imdb script. First run the imdb script, then copy
       and paste the results in the assert statement below. Finally run this test script. If 
       successful, the message "Everything Passed" will be printed.
    """
    assert imdb.imdb("predator")[0] == "Xtinction: Predator X"

def test_ott():
    """This method will test the ott script. First run the ott script, then copy
       and paste the results in the assert statement below. Finally run this test script. If 
       successful, the message "Everything Passed" will be printed.
    """
    assert ott.ott("titanic")[0] == "Back to the Titanic"


if __name__ == "__main__":
    test_platform()
    test_youtube()
    test_ott()
    imdb_id()
    print("Everything passed")