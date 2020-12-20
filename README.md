# Movie-app

DESCRIPTION

A Simple movie app made with python. The app displays a menu of different streaming media services to choose from which will provide the metadata of a movie or Tv show for that movie or tv show entered by the user. The application also includes a watchlist that will contain any movies or TV shows watched by the user and will make recommendations based on the movies watched.


QUICK START

Open the containing folder, to run the project use the terminal and run: python movie_selector_current.py
and then it will display the menu.

Select from the menu of streaming media platforms:
1. Youtube
2. ott
3. imdb
4. Exit

****************************************************************
YOUTUBE API - 
If the user selects 1, the following message will appear:

```"Youtube has been selected"```


Then it will prompt the user to do the following:

```Enter in the Movie Title or TV Show: peppermint```

Once the title is enter, it will display the results below:
```
Title: Peppermint Trailer #1 (2018) | Movieclips Trailers

Like_Ratio: 95.54

URL: https://i.ytimg.com/vi/eeBMQpzoEXQ/default.jpg
```

Once the results are displayed, the menu will print again.
*****************************************************************




***************************************************************************************************************
OTT API
If the user selects 2, the following message will appear:

```"ott has been selected"```

Then it will prompt the user to do the following:

```Enter in the Movie Title or TV Show: Titanic```

Once the title is enter, it will display the results below:
```
Title: Back to the Titanic

Year: 2020

Synopsis: Back to the Titanic documents the first manned dives to Titanic in nearly 15 years. New footage reveals fresh decay and sheds light on the ship's future.

Image: ['https://m.media-amazon.com/images/M/MV5BNTI4ZTM2ZjgtYWI4OS00MTViLWIwYmUtMTljZmYxMjA4NWRhXkEyXkFqcGdeQXVyMTk1MDMwNjk@._V1_UY268_CR147,0,182,268_AL__QL50.jpg']
```
Once the results are displayed, the menu will print again.
***************************************************************************************************************




**************************************************************
IMDB API
If the user selects 3, the following message will appear:

```"imdb has been selected"```

Then it will prompt the user to do the following:

```Enter in the Movie Title or TV Show: Die hard```

Once the title is enter, it will display the results below:
```
Title: Live Free or Die Hard

Year: 2007

IMDB_ID: tt0337978
```
Once the results are displayed, the menu will print again.
***************************************************************




*************************************************************************************************************
If user selects any number besides the ones in the menu, an error message will be raised and the program will display the following:

```"Wrong option selection. Please select from the menu..."```
**************************************************************************************************************



*****************************************************************************
Finally, when the user selects number 4 in the menu, it will end the program.
*****************************************************************************









