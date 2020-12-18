import requests
import json
import pprint

def Netflix():
    """This method will search the Netflix API for information about the title of the movie (Simrat Kaur).
    
    Returns:
        The title, genre, summary, and director name, of the movie.
    """
    
    result = input("Enter in Movie Title:")

    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"t":"loadvideo","q":"60029591"}

    headers = {
        'x-rapidapi-key': "b08ebf0eb1msh1a42bdbfe0d3d70p138554jsn9e81d1deb388",
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring) 
    
      
    print(response.text)
    

if __name__ == "__main__":
    Netflix()