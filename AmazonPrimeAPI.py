import requests
import time
import json
import pprint


def Amazon():
#Samantha Kamal
    """This method will search the Amazon Prime Video API for information about the title of the movie (Simrat Kaur).
        
    Returns:
            The title, genre, summary, and director name, of the movie.
    """


    result = input("Enter in Movie or Tv Show Title: ")

    url = "https://streamzui-streamzui-v1.p.rapidapi.com/" + result

    """URL for Amazon Prime Video API via Rapid API"""

    querystring = {"page":"1","country":"us","type":"Movie"}

    headers = {
        'x-rapidapi-key': "54e93237a1msh975f4560b132a79p19bb2ajsn83d84344d274",
        'x-rapidapi-host': "streamzui-streamzui-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonResponse = response.json()
    #pprint.pprint(jsonResponse)
    for item in jsonResponse:
        api_Title = jsonResponse["Results"][0]["Title"]
        api_Link = jsonResponse["Results"][0]["Link"]
        api_Year = jsonResponse["Results"][0]["Year"]

    return api_Title, api_Link, api_Year


#pprint.pprint(response.text)

if __name__ == "__main__":
    print(Amazon()[0])
