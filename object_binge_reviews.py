"""
    TV Show Specifications, Adds and Displays specifications within a TVShow object.
    Object Oriented Programming Lab 3
    Austin Banner
    10/22/23
"""
from TVShow import TVShow

def read_shows(file_name: str) -> list[TVShow]:
    """Takes the ratings for a show and returns the average."""
    avg: float = 0
    if (len(ratings) > 0):
        for i in ratings:
            avg = sum(ratings)
        avg = avg/len(ratings)
    # If no ratings exist, returns -1.
    else:
        avg = -1
    return ("{:.2f}".format(avg))

def read_shows(file_name: str) -> list[TVShow]:
    """Read show data from the file passed in, and
        assemble into a list of TVShows and return."""
    # Creates a list of TVShows.
    shows: list[TVShow] = []
    # Opens the file to be read.
    file = open(file_name, "r")

    # Title is the first line within the file.
    title: str = file.readline()
    title = title.strip()

    # While title is not empty, read the rest of the file.
    while(title != ""):
            # Assigns the show data to variables.
            num_seasons: int = int(file.readline())
            genre: str = file.readline()

            # Converts line into a list of integers for ratings.
            rating_line: str = file.readline()
            rating_line = rating_line.strip()
            ratings: list = rating_line.split(",")
            if(rating_line != ''):
                ratings = [int(i) for i in ratings]
            else:
                ratings = []
            # Converts line into a list of strings for hashtags.
            hashtag_line: str = file.readline()
            hashtag_line = hashtag_line.strip()
            hashtags:list = hashtag_line.split(",")

            # Creates a list with the data.
            show: TVShow = TVShow(title,
                 num_seasons,
                 genre,
                 ratings,
                 hashtags)

            # Adds the show to list of shows.
            shows.append(show)

            title = file.readline()
            title = title.strip()

    return shows

def menu(shows_list: list[TVShow]) -> None:
    """ Displays a menu and calls a function based on selection until quit."""
    choice:int = 0
    options: list = [1,2,3,4,5]
    while(choice != 5):
        print("1. Display all show titles")
        print("2. Find shows")
        print("3. Add tag")
        print("4. Add rating")
        print("5. Quit")

        # If invalid choice, get a new choice.
        choice = int(input("Please enter your choice: "))
        while(choice not in options):
            choice = int(input("Invalid choice, try again: "))

        # Calls a function based on seleciton, passing the list of TVShows.
        if(choice == 1):
            display_shows(shows_list)
        elif(choice == 2):
            find_shows(shows_list)
        elif(choice == 3):
            add_tag(shows_list)
        elif(choice == 4):
            add_rating(shows_list)
            

def display_shows(shows_list: list[TVShow]) -> None:
    """Displays the titles of every TVShow object. """
    i: int = 0
    # Get title while there is still another TVShow. 
    while(i < len(shows_list)):
        print(shows_list[i].get_title())
        i += 1

def find_shows(shows_list: list[TVShow]) -> None:
    """Checks if the tag exists within a TVShow, if it does, prints the title. """
    tag: str = input("Please enter the tag you want to search for: ") 
    i: int = 0
    while(i < len(shows_list)):
        if(shows_list[i].is_tagged(tag)):
            print(shows_list[i].get_title())
        i += 1

def add_tag(shows_list: list[TVShow]) -> None:
    """Lets user add a hashtag to a specific show. """
    title:str = input("Please enter the title of the show you want to tag: ")
    tag: str
    found: bool = False
    i: int = 0
    while(i < len(shows_list)):
        # Finding the title of the show within the list.
        # If found, adds the hashtag to that shows list of hashtags, printing results.
        if(title == shows_list[i].get_title()):
            found = True
            tag = input("Enter the tag: ")
            shows_list[i].add_hashtag(tag)
            print(shows_list[i])
        i += 1
    # If show is not found, print the error.
    if(found == False):
        print("TV Show not found ")

def add_rating(shows_list: list[TVShow]) -> None:
    """Lets user add a rating to a specific show. """ 
    title:str = input("Which show would you like to add a rating to: ")
    rating: int
    found: bool = False
    i: int = 0
    while(i < len(shows_list)):
        # Finding the title of the show within the list.
        # IF found, adds the rating to that shows list of ratings, printing results.
        if(title == shows_list[i].get_title()):
            found = True
            rating = int(input("Enter the rating: "))
            shows_list[i].add_rating(rating)
            print(shows_list[i])
        i += 1
        # If show title is not found, prints an error.
    if(found == False):
        print("TV Show not found ")
            
def main() -> None:
    """Reads in the list of TVShows using a file name.
       Calls the menu to display options.
    """
    shows_list: list[TVShow] = read_shows("shows.txt")
    menu(shows_list)
                        
main()
