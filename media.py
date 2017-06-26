#webbrowser is imported so program can run in a web browser
import webbrowser

#Class Movie is defined and the class variables are listed. 
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title  = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
#Web browser is instructed to open the movies' youtube urls
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    
        
