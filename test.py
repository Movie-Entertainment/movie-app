
from movie_selector import Entertainment
import unittest

def test_platform():
    my_entertainment = Entertainment()
    assert my_entertainment.platform == None

def test_youtube():
    my_entertainment = Entertainment()
    assert my_entertainment.lookup_youtube("predator") != None

def test_amazon():
    my_entertainment = Entertainment()
    assert my_entertainment.lookup_amazon("predator") != None

def test_netflix():
    my_entertainment = Entertainment()
    assert my_entertainment.lookup_netflix("predator") != None


if __name__ == "__main__":
    test_platform()
    test_youtube()
    test_amazon()
    test_netflix()
    print("Everything passed")