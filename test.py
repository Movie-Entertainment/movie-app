
from movie_selector_current import Entertainment
import unittest
import youtube
import imdb
import ott


def test_platform():
    my_entertainment = Entertainment()
    assert my_entertainment.platform == None
    assert my_entertainment.result == None

def test_youtube():
    assert youtube.lookup_youtube("peppermint")[0] == "Peppermint Trailer #1 (2018) | Movieclips Trailers"

def imdb_id():
    assert imdb.imdb("predator")[0] == "Xtinction: Predator X"

def test_ott():
    assert ott.ott("titanic")[0] == "Back to the Titanic"


if __name__ == "__main__":
    test_platform()
    test_youtube()
    test_ott()
    imdb_id()
    print("Everything passed")