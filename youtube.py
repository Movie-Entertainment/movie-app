
import requests
import json
import pprint

def lookup_youtube(search):
    """Searching youtube api to extract the following:
            1. Title of the movie
            2. likes and dislikes for the movie.
            3. image of the movie
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
        return apiResult, api_ratio, api_image #returns 3 pieces of data. access the data (0, 1, 2)
    

#def youtube_url:
    
if __name__ == "__main__":
    print(lookup_youtube("peppermint")[2])