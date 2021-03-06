import requests
import json
import pprint

def imdb(result):
    """This method will search the imdb api for the metadata
        of the movie or tv show entered and extract the following:
            1. Title of the movie
            2. Year of the movie
            3. The imdb ID of the movie
            
    Args:
        result (str): the result.
            
    Returns:
        The title, year, and imdb id of a movie.
    """
    url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

    querystring = {"type":"get-movies-by-title","title": result}

    headers = {
        'x-rapidapi-key': "979499eb08msh3664a876cdc17fcp17f3adjsnde10b912d78f",
        'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonResponse = response.json()
    #used len here because the movie we selected appeared at the bottom of the list.
    api_Title = jsonResponse["movie_results"][len(jsonResponse["movie_results"])- 1]["title"]
    api_Year = jsonResponse["movie_results"][len(jsonResponse["movie_results"])- 1]["year"]
    api_imdb_id = jsonResponse["movie_results"][len(jsonResponse["movie_results"])- 1]["imdb_id"]
    
    return api_Title, api_Year, api_imdb_id
    #pprint.pprint(jsonResponse)

if __name__ == "__main__":
    print(imdb("predator")[0])