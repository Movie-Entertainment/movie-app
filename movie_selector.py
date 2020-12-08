import sys
import requests
import json
import youtube_api
import hulu_api
import amazon_prime_api


class Entertainment():
    """This function gives the user options for choosing a movie platform
    where they would like to see a certain movie or tv show (Zarlashta Manan).
    """
    
    def __init__(self):
        self.platform = None

    def lookup_all(self):
        result = input("Enter in the Movie Title or TV Show:")

    # def lookup_amazon(self):
    #     result = input("Enter in the Movie Title or TV Show:")

    # def lookup_hulu(self):
    #     result = input("Enter in the Movie Title or TV Show:")

    # def lookup_youtube(self):
    #     result = input("Enter in the Movie Title or TV Show:")
    #     url = "https://youtube-search1.p.rapidapi.com/" + result

    #     headers = {
    #     'x-rapidapi-key': "3d2fbbd54bmshbbccc15fd8196c7p11c1aejsn36237f19f62b",
    #     'x-rapidapi-host': "youtube-search1.p.rapidapi.com"
    #              }

    #     response = requests.request("GET", url, headers=headers)
    #     jsonResponse = response.json()
    #     print("******************************************")
    #     for key, value in jsonResponse.items():
    #         print(jsonResponse["items"][0]["title"])

    #     print("******************************************")

        
    def print_menu(self):  ## Your menu design here
        print("1. Youtube")
        print("2. Hulu")
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
                self.platform = "Youtube"
                self.lookup_youtube()

            elif choice==2:
                print("Hulu has been selected")
                self.platform = "Hulu"
                self.lookup_hulu()
       
            elif choice==3:
                print("Amazon_Prime has been selected")
                self.platform = "Amazon_Prime"
                self.lookup_amazon()
        
            elif choice==4:
                print("All has been selected")
                self.platform = "All"
                self.lookup_hulu()
                self.lookup_amazon()
                self.lookup_youtube()
        
            elif choice==5:
                print("Menu 5 has been selected")
                loop=False # This will make the while loop to end as not value of loop is set to False
            else:
            # Any integer inputs other than values 1-5 we print an error message
                print("Wrong option selection. Enter any key to try again..")
            
    

if __name__ == "__main__":
    my_entertainment = Entertainment()
    my_entertainment.start_program()
    






