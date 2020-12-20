import requests
import json
import pprint

def ott(search):
    """This method will search the ott api for the metadata
        of the movie or tv show entered and extract the following:
            1. Title of the movie
            2. Year of the movie
            3. Synopsis of the movie
            4. Image of the movie
            
    Returns:
        The title, year, synopsis, and image of a movie.
    """

    url = "https://ott-details.p.rapidapi.com/search"

    querystring = {"title": search,"page":"1"}

    headers = {
        'x-rapidapi-key': "979499eb08msh3664a876cdc17fcp17f3adjsnde10b912d78f",
        'x-rapidapi-host': "ott-details.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonResponse = response.json()
    api_Title = jsonResponse["results"][0]["title"]
    api_Year = jsonResponse["results"][0]["released"]
    api_synopsis = jsonResponse["results"][0]["synopsis"]
    api_image = jsonResponse["results"][0]["imageurl"]
    
    return api_Title, api_Year, api_synopsis, api_image


if __name__ == "__main__":
     print(ott("titanic")[2])