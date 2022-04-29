#########################################
##### Name: Arjun Ananda Padmanabhan #####
##### Uniqname: aarjun               #####
#########################################

import json
import requests
import webbrowser
import time

#### PART 1 ####

# class Media:

#     def __init__(self, title="No Title", author="No Author", release_year = "No Release Year", url="No URL"):
#         self.title = title
#         self.author = author
#         self.release_year = release_year
#         self.url = url

#     def info(self):
#         return f"{self.title} by {self.author} ({self.release_year})"

#     def length(self):
#         return 0

# class Song(Media):
#     def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No genre", track_length=0):
#         super().__init__(title, author, release_year, url)
#         self.album = album
#         self.genre = genre
#         self.track_length = track_length
    
#     def info(self):
#         return super().info() + f"[{self.genre}]"

#     def length(self):
#         time_in_s = round(self.track_length / 1000)
#         return time_in_s 

# class Movie(Media):
#     def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0):
#         super().__init__(title, author, release_year, url)
#         self.rating = rating
#         self.movie_length = movie_length

#     def info(self):
#         return super().info() + f"[{self.rating}]"

#     def length(self):
#         time_in_min = round(self.movie_length/60000)
#         return time_in_min
# Other classes, functions, etc. should go here

#### PART 2-4 ####

class Media:
    '''A media's information container
    Attributes
    ----------
    title: string
        The media's title
    author: string
        The media's author
    release_year: string
        the media's release year
    url: string
        the median's link
    json: dictionary
        media information in json form
    
    Methods:
        info: Returns the basic information.
        length: Return media's length, default 0. 
    '''

    def __init__(self, title="No Title", author="No Author", release_year = "No Release Year", url="No URL", json=None):
        if json:
            if json.get('wrapperType') == 'track':
                self.title = json.get("trackName") 
                self.url = json.get('trackViewUrl')
            else:
                self.title = json.get("collectionName")
                self.url = json.get("collectionViewUrl")
            self.author = json.get('artistName')
            self.release_year = json.get('releaseDate').split('-')[0]

        else:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url

    def info(self):
        '''Return media's basic information.
        Parameters
        ----------
        none
        Returns
        -------
        string
            contain media's title, author and release year
        '''
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        '''Return media's length.
        Parameters
        ----------
        none
        Returns
        -------
        int
            media's length, default 0.
        '''
        return 0
        
class Song(Media):
    '''A song's information container
    Attributes
    ----------
    title: string
        The song's title
    author: string
        The song's author
    release_year: string
        the song's release year
    url: string
        the song's link
    album: string
        the song's album
    genre: string
        the song's genre
    track_length: int
        song's length in millisecond.
    json: dictionary
        song information in json form

    Methods:
        info: Returns the basic information.
        length: Return song's length in seconds. 
    '''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No genre", track_length=0, json=None):
        super().__init__(title, author, release_year, url, json)
        if json:
            self.album = json.get('collectionName')
            self.genre = json.get('primaryGenreName')
            self.track_length = json.get('trackTimeMillis')
        else:
            self.album = album
            self.genre = genre
            self.track_length = track_length
        
    def info(self):
        '''Return song's basic information.
        Parameters
        ----------
        none
        Returns
        -------
        string
            contain song's title, author, release year and genre
        '''
        return super().info() + ' ' + f"[{self.genre}]"

    def length(self):
        '''Return song's length.
        Parameters
        ----------
        none
        Returns
        -------
        int
            song's length in seconds (rounded to nearest second).
        '''
        time_in_s = round(self.track_length / 1000)
        return time_in_s 

class Movie(Media):
    '''A movie's information container
    Attributes
    ----------
    title: string
        The movie's title
    author: string
        The movie's author
    release_year: string
        the movie's release year
    url: string
        the movie's link
    rating: string
        the movie's rating
    movie_length: int
        movie's length in millisecond.
    json: dictionary
        movie information in json form
    
    Methods:
        info: Returns the basic information.
        length: Return movie's length in minutes. 
    '''
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0, json=None):
        super().__init__(title, author, release_year, url, json)
            
        if json:
            self.rating = json.get('contentAdvisoryRating')
            self.movie_length = json.get('trackTimeMillis')
        else:
            self.rating = rating
            self.movie_length = movie_length


    def info(self):
        '''Return movie's basic information.
        Parameters
        ----------
        none
        Returns
        -------
        string
            contain movie's title, author, release year and rating
        '''
        return super().info() + ' ' + f"[{self.rating}]"

    def length(self):
        '''Return movie's length.
        Parameters
        ----------
        none
        Returns
        -------
        int
            movie's length in minutes (rounded to nearest minute).
        '''
        time_in_min = round(self.movie_length/60000)
        return time_in_min


def get_resource(url, params=None):
    """Returns a response object decoded into a dictionary. If query string < params > are
        provided the response object body is returned in the form on an "envelope" with the data
        payload of one or more itunesAPI entities to be found in ['results'] list; otherwise, response
        object body is returned as a single dictionary representation of the itunesAPI entity.
    
        Parameters:
            url (str): a url that specifies the resource.
            params (dict): optional dictionary of querystring arguments.
    
        Returns:
            dict: dictionary representation of the decoded JSON.
        """
    if params:
        return requests.get(url, params, timeout=10).json()
    else:
        return requests.get(url, timeout=10).json()

class get_data():
    '''A movie's information container
    Attributes
    ----------
    user_input : The input of the user for search term. 
    
    Methods:
        get_source: Returns list of songs, movies and other medias for user input. 
        itunes_output: Return the URL and opens the web browser for the user input.
    '''
    def __init__(self, user_input):
        self.user_input = user_input
        

    def get_source(self):
        """Returns a list of song, movie and audiobook extracted from the itunes API in a 
        orderly manner (SONG->MOVIE->OTHERMEDIA). The iteration runs through the 
        decoded JSON dictionary (from iTunes API ) and the result (info and url) is stored in the respective 
        lists (Song, movie, audiobook) as a tuple. 
    
        Parameters:
            None
    
        Returns:
            list of Song, Movie and audiobook
        """

        url = 'https://itunes.apple.com/search?parameterkeyvalue'
        params = {'term': self}

        itune_data = get_resource(url, params=params)['results']

        global song
        global movie
        global audiobook

        song = [ ]
        audiobook = [ ]
        movie = [ ]
    

        for item in itune_data:
                
                if item.get('kind') == 'song':
                    a = Song(json=item)
                    song.append((a.info(), a.url))
                    # song_url.append(a.url)
                
                elif item.get('wrapperType') == 'audiobook' :
                    c = Song(json=item)
                    audiobook.append((c.info(), c.url))
            
            
                elif item.get('kind') == 'feature-movie':
                        b = Movie(json=item)
                        movie.append((b.info(), b.url))
    

        song = list(set(song))
        movie = list(set(movie))
        audiobook = list(set(audiobook))


        print("\n SONGS\n")
        if len(song) >0:
                for item in song:
                    print (f"{song.index(item)+1} {item[0]}\n")
        else:
                print("There are no Songs for this search term")

        print("\n MOVIES \n")
        if len(movie) >0:
                for item in movie:
                    print (f"{movie.index(item)+len(song)+1} {item[0]}\n")
        else:
                print("There are no movies for this search term")
            
        print("\n OTHER MEDIA \n")
        if len(audiobook) >0:
                for item in audiobook:
                    print (f"{audiobook.index(item)+(len(song)+len(movie)+1)} {item[0]}\n")
        else:
                print("There are no other medias for this search term")


    def itunes_output(self):
        """
        Checks if user input is there in the index of lists (song, movie and audiobook) 
        and returns the corresponding URL for the user input. Also the function
        opens the URL in the web browser. 

        Parameters:
            None
    
        Returns:
            Returns the URL if the URL is there in the index of lists (song, movie and audiobook) and
            launches web browser for the provided input. 
            If the user input is 0 or more than the index of the combined list, then an error message
            is returned. 
        """
        if self < 1 or self > len(song) + len(movie) + len(audiobook):
            print(f"Please enter a valid input from 1 to {len(song) + len(movie) + len(audiobook)}")

        elif self <= len(song):
            print(f"Launching:\n {song[self-1][1]} \n in web browser...")
            time.sleep(3)
            webbrowser.open(song[self-1][1])

        elif self <= (len(song) + len(movie)) and self > (len(song)) :
            x = self - len(song)
            print(f"Launching:\n {movie[x-1][1]} \n in web browser...")
            time.sleep(3)
            webbrowser.open(movie[x-1][1])

        else:
            x = self - (len(song) + len(movie))
            print(f"Launching:\n {audiobook[x-1][1]} \n in web browser...")
            time.sleep(3)
            webbrowser.open(audiobook[x-1][1])


if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    
    # movie = Media()
    # movie.author = "David Brown"
    # movie.release_year = 1997
    # movie.title = "Yes"

    # print(movie.info())


    # song = Song()
    # song.title = "Yes My Love"
    # song.author = "Britney Spears"
    # song.release_year = "1997"
    # song.track_length = 1983
    # song.genre = "Pop"

    # print(song.info())

    # movi = Movie()
    # movi.title = "Jurassic Park"
    # movi.author = "David Cameron"
    # movi.release_year = "1998"
    # movi.rating = "PG"
    # movi.movie_length = 8273873

    # print(movi.info())
    # print(movi.length())
    # print(song.length())



    # f = open("sample_json.json")
    # sample = json.loads(f.read())
    # f.close()

    # test = Movie(json=sample[0])

    # print(test.info())




    user_input = input("Enter a search term, or exit to quit:")
    data = str(user_input)

    while (data.lower().strip(' ') != 'exit'):
            itunes_output = get_data.get_source(data.strip(' '))
            user_input2 = input("\nEnter a number for more info, or another search term, or exit:")

            if user_input2.strip(' ').isnumeric():
                        x = get_data.itunes_output(int(user_input2.strip(' ')))
                        continue
            else:
                        data = str(user_input2.strip(' '))

    print("\nThank you for using the iTunes search engine")




