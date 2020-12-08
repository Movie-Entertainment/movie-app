import sys
import requests
import json


class Entertainment():
    """This function gives the user options for choosing a movie platform
    where they would like to see a certain movie or tv show (Zarlashta Manan).
    """
    
    def __init__(self):
        self.platform = None

    def lookup_all(self, result):
        self.lookup_youtube(result)
        self.lookup_amazon(result)
        self.lookup_netflix(result)

    def lookup_amazon(self,result):

        apiResult = None
        url = "https://streamzui-streamzui-v1.p.rapidapi.com/search"

        querystring = {"country":"us","page":"1","type":"Movie"}

        headers = {
        'x-rapidapi-key': "54e93237a1msh975f4560b132a79p19bb2ajsn83d84344d274",
        'x-rapidapi-host': "streamzui-streamzui-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        jsonResponse = response.json()
        print(jsonResponse)
        for key, value in jsonResponse.items():
            print("Amazon title:" + jsonResponse["Results"][0]["Title"])
            print("Amazon link:" + jsonResponse["Results"][0]["Link"])
            apiResult = jsonResponse["Results"][0]["Link"]

        return apiResult

    def lookup_netflix(self, result):
      
        apiResult = None
        url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

        querystring = {"t":"loadvideo","q":"60029591"}

        headers = {
        'x-rapidapi-key': "b08ebf0eb1msh1a42bdbfe0d3d70p138554jsn9e81d1deb388",
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring) 
      
        print(response.text)
       
        jsonResponse = response.json()
      
        print("Netflix title:" + jsonResponse["RESULT"]["nfinfo"]["title"])
        print("Netflix link:" + jsonResponse["RESULT"]["nfinfo"]["image1"])
        apiResult = jsonResponse["RESULT"]["nfinfo"]["title"]

        return apiResult

    def lookup_youtube(self, search):
   
        apiResult = None
        url = "https://youtube-search1.p.rapidapi.com/" + search
        headers = {
        'x-rapidapi-key': "3d2fbbd54bmshbbccc15fd8196c7p11c1aejsn36237f19f62b",
        'x-rapidapi-host': "youtube-search1.p.rapidapi.com"
                 }

        response = requests.request("GET", url, headers=headers)
        jsonResponse = response.json()
        print("******************************************")
        for key, value in jsonResponse.items():
            print("You tube link:" + jsonResponse["items"][0]["description"])
            print("You tube title:" + jsonResponse["items"][0]["title"])
            apiResult = jsonResponse["items"][0]["title"]

        print("******************************************")

        return apiResult

    def print_menu(self):  ## Your menu design here
        print("1. Youtube")
        print("2. Netflix")
        print("3. Amazon_Prime")
        print("4. All")
        print("5. Exit")
    
    def start_program(self):
        loop=True      
  
        while loop:  ## While loop which will keep going until loop = False
            
            self.print_menu()    ## Displays menu
            choice = int(input("Enter your choice [1-5]: "))
     
            if choice==1:     
                print("Youtube has been selected")
                result = input("Enter in the Movie Title or TV Show:")
                
                self.platform = "Youtube"
                self.lookup_youtube(result)

            elif choice==2:
                print("Netflix has been selected")
                result = input("Enter in the Movie Title or TV Show:")
                self.platform = "Netflix"
                self.lookup_netflix(result)
       
            elif choice==3:
                print("Amazon_Prime has been selected")
                result = input("Enter in the Movie Title or TV Show:")
                self.platform = "Amazon_Prime"
                self.lookup_amazon(result)
        
            elif choice==4:
                print("All has been selected")
                result = input("Enter in the Movie Title or TV Show:")
                self.platform = "All"
                self.lookup_all(result)
                
        
            elif choice==5:
                print("Menu 5 has been selected")
                loop=False # This will make the while loop to end as not value of loop is set to False
            else:
            # Any integer inputs other than values 1-5 we print an error message
                print("Wrong option selection. Please select from the menu options.")
                

if __name__ == "__main__":
    my_entertainment = Entertainment()
    my_entertainment.start_program()
    






