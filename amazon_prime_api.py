import requests
import json
import time

def amazon_prime():

    url = "https://streamzui-streamzui-v1.p.rapidapi.com/search"

    querystring = {"country":"us","page":"1","type":"Movie"}

    headers = {
    'x-rapidapi-key': "54e93237a1msh975f4560b132a79p19bb2ajsn83d84344d274",
    'x-rapidapi-host': "streamzui-streamzui-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    
if __name__ == "__main__":
    amazon_prime()