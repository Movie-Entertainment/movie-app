import sys
import requests
import json

import youtube
import ott
import imdb


class Entertainment():
    """This function gives the user options for choosing a movie platform
    where they would like to see a certain movie or tv show (Zarlashta Manan).
    """
    
    def __init__(self):
        self.platform = None
        self.result = None

    # def lookup_all(self, result):
    #     self.lookup_youtube(result)
    #     self.lookup_imdb(result)
    #     self.lookup_netflix(result)


    
    def print_menu(self):  ## Your menu design here
        print("1. Youtube")
        print("2. ott")
        print("3. imdb")
        print("4. Exit")
        
    
    def start_program(self):
        loop=True      
  
        while loop:  ## While loop which will keep going until loop = False
            
            self.print_menu()    ## Displays menu
            choice = int(input("Enter your choice [1-4]: "))
     
            if choice==1:     
                print("Youtube has been selected")
                self.result = input("Enter in the Movie Title or TV Show:")
                self.platform = "Youtube"
                youtube_data = youtube.lookup_youtube(self.result)
                print(f'Title: {youtube_data[0]}\n')
                print(f'Like_Ratio: {youtube_data[1]}\n')
                print(f'URL: {youtube_data[2]}')
                
            elif choice==2:
                print("ott has been selected")
                self.result = input("Enter in the Movie Title or TV Show:")
                self.platform = "ott"
                ott_database = ott.ott(self.result)
                print(f'Title: {ott_database[0]}\n')
                print(f'Year: {ott_database[1]}\n')
                print(f'Synopsis: {ott_database[2]}\n')
                print(f'Image: {ott_database[3]}')

                
            elif choice==3:
                print("imdb has been selected")
                self.result = input("Enter in the Movie Title or TV Show:")
                self.platform = "imdb"
                movie_database = imdb.imdb(self.result)
                print(f'Title: {movie_database[0]}\n')
                print(f'Year: {movie_database[1]}\n')
                print(f'IMDB_ID: {movie_database[2]}')
        
            # elif choice==4:
            #     print("All has been selected")
            #     self.result = input("Enter in the Movie Title or TV Show:")
            #     self.platform = "All"
            #     self.lookup_all(self.result)
                
        
            elif choice==4:
                print("Program Ends!")
                loop=False # This will make the while loop to end as not value of loop is set to False
            else:
            # Any integer inputs other than values 1-5 we print an error message
                print("Wrong option selection. Please select from the menu...")
                

if __name__ == "__main__":
    my_entertainment = Entertainment()
    my_entertainment.start_program()
    
    






