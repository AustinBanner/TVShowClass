"""
    TV Show Class
    Creates a TVShow with specifications that can be edited.
    Austin Banner
    10/22/23
"""
import io
import os.path
class TVShow():

    # Annotate object-level fields
    _title: str
    _num_seasons: int
    _genre: str
    _ratings: list[int]
    _hashtags: list[str]

    def __init__(self, title: str, num_seasons: int, genre: str,
                 ratings: list[int], hashtags: list[str]) -> None:
            """ Creating TVShow with specifications. """

            self._title = title
            self._num_seasons = num_seasons
            self._genre = genre
            self._ratings = ratings
            self._hashtags = hashtags

    def get_average_rating(self) -> float:
        """Takes the ratings for a show and returns the average."""
        avg: float = 0
        if (len(self._ratings) > 0):
            for i in self._ratings:
                avg = sum(self._ratings)
            avg = avg/len(self._ratings)
        # If no ratings exist, returns -1.
        else:
            avg = -1
        return (avg)

    def is_tagged(self, tag: str) -> bool:
        """Checks if the given tag is within the TVShow. """
        tagged: bool = False
        if tag in self._hashtags:
            tagged = True
        return tagged

    def get_num_seasons(self) -> int:
        """Gets the number of seasons within the TVShow. """
        return self._num_seasons

    def get_genre(self) -> str:
        """Gets the genre of the TVShow. """
        return self._genre

    def get_title(self) -> str:
        """Gets the title of the TVShow. """
        return self._title

    def add_rating(self, new_rating:int) -> None:
        """Adds a rating to the list of ratings for the TVShow. """
        self._ratings.append(new_rating)

    def add_hashtag(self, new_tag:str) -> None:
        """Adds a hastag to list if not currently present. """
        if(new_tag in self._hashtags):
            print(new_tag + " is already a hashtag. ")
        else:
            self._hashtags.append(new_tag)

    def __str__(self) -> str:
        """Return a string representation of the object."""
        result: str = "{:15s}: {:s}\n".format("Title",self._title)
        result += "{:15s}: {:d}\n".format("Seasons",self._num_seasons)
        result += "{:15s}: {:s}".format("Genre",self._genre)
        rating: float = self.get_average_rating()
        if rating != -1:
            result += "{:15s}: {:.2f}\n".format("Rating",rating)
        else:
            result += "{:15s}: {:s}\n".format("Rating","No ratings")
        result += "{:15s}: {:s}\n".format("Tags",str(self._hashtags))
        return result

    
        
