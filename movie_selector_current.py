import sys
import requests
import json

import youtube
import ott
import imdb


class Entertainment():
    """This function gives the user options for choosing a movie platform
    where they will be able to enter a specific movie or tv show and receive
    different types of information such as the year, description,
    image and so on depending on what the api provides. 
    
    Attributes:
        platform (str): streaming media services.
        result (str): the results.
    """
    
    def __init__(self):
        """Initializes the class variables.
        
        Args:
            platform (str): see class documentation.
            result (str): see class documentation.
        """
        self.platform = None
        self.result = None

    # def lookup_all(self, result):
    #     self.lookup_youtube(result)
    #     self.lookup_imdb(result)
    #     self.lookup_netflix(result)
    
    def print_menu(self):  
        """This method will print a menu that contains the streaming media 
           services options. It will also print an option to exit the program. 
        """
        print("1. Youtube")
        print("2. ott")
        print("3. imdb")
        print("4. Exit")
        
        
    def start_program(self):
        """This method will start the program. It will allow user to choose a platform 
           from the menu and then the user can enter in a movie or tv show. Then it will 
           use the apis imported from their individual scripts and extract the data for 
           that movie or tv show. For each platform, it will print different information
           depending on what the api provided. User also has an option to exit
           the program.
           
        Raises:
            ValueError: If a user enters in any number other than the value 1-4, an
            error message will be printed asking the user to try again.
        """
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
            # Any integer inputs other than values 1-4 we print an error message
                print("Wrong option selection. Please select from the menu...")
                

if __name__ == "__main__":
    my_entertainment = Entertainment()
    my_entertainment.start_program()
    
    






