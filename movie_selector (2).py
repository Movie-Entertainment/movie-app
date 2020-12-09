import sys
import requests
import json

import youtube
import netflix
import amazon


class Entertainment():
    """This function gives the user options for choosing a movie platform
    where they would like to see a certain movie or tv show (Zarlashta Manan).
    """
    
    def __init__(self):
        self.platform = None
        self.result = None

    def lookup_all(self, result):
        self.lookup_youtube(result)
        self.lookup_amazon(result)
        self.lookup_netflix(result)

    
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
                self.result = input("Enter in the Movie Title or TV Show:")
                
                self.platform = "Youtube"
                print(youtube.lookup_youtube(self.result))
                #print(youtube.lookup_youtube(f'Title: , Ratio: , Image: '))

            elif choice==2:
                print("Netflix has been selected")
                self.result = input("Enter in the Movie Title or TV Show:")
                self.platform = "Netflix"
                print(netflix.lookup_netflix(self.result))
       
            elif choice==3:
                print("Amazon_Prime has been selected")
                self.result = input("Enter in the Movie Title or TV Show:")
                self.platform = "Amazon_Prime"
                print(amazon.lookup_amazon(self.result))
        
            elif choice==4:
                print("All has been selected")
                self.result = input("Enter in the Movie Title or TV Show:")
                self.platform = "All"
                self.lookup_all(self.result)
                
        
            elif choice==5:
                print("Program Ended!")
                loop=False # This will make the while loop to end as not value of loop is set to False
            else:
            # Any integer inputs other than values 1-5 we print an error message
                print("Wrong option selection. Please select from the menu...")
                

if __name__ == "__main__":
    my_entertainment = Entertainment()
    my_entertainment.start_program()
    
    






