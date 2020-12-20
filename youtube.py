
import requests
import json
import pprint

def lookup_youtube(search):
    """This method will search the youtube api for the metadata
        of the movie or tv show entered and extract the following:
            1. Title of the movie
            2. The ratio of the likes and dislikes for the movie
            3. The image of the movie:
            
    Returns:
        The title, ratio of likes and dislikes, and the image of a movie.
    """  
    apiResult = None
    url = "https://youtube-search1.p.rapidapi.com/" + search
    headers = {
    'x-rapidapi-key': "3d2fbbd54bmshbbccc15fd8196c7p11c1aejsn36237f19f62b",
    'x-rapidapi-host': "youtube-search1.p.rapidapi.com"
                }

    response = requests.request("GET", url, headers=headers)
    jsonResponse = response.json()
    for key, value in jsonResponse.items():
        apiResult = jsonResponse["items"][0]["title"]
        api_likes = int(jsonResponse["items"][0]["likeCount"]) 
        api_dislikes = int(jsonResponse["items"][0]["dislikeCount"])  
        api_image = jsonResponse["items"][0]["thumbDefault"]
    api_ratio = round((api_likes/(api_dislikes + api_likes)) * 100, 2)
    return apiResult, api_ratio, api_image #returns 3 pieces of data (title, ratio of likes and dislikes and image). access the data (0, 1, 2)
    
if __name__ == "__main__":
    print(lookup_youtube("spy kids")[2])