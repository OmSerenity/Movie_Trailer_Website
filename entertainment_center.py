#import fresh_tomatoes file for website formatting 
import fresh_tomatoes
#import media file for classes
import media

#Listing of Title, Storyline, Movie Image, and Youtube trailers to be applied for each movie
#When run, title and the storyline will print in the Python shell, separated by a blank line
#Website will then load in the browser in which the movie's title appears under the movie image
#When movie image is clicked, movie's Youtube trailer will play

sing = media.Movie("Sing",
            "Hopeful singers compete in a singing contest",
            "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
            "https://youtu.be/m37yG_7UXRM")
print(sing.title)
print(sing.storyline)
#print without an argument for each movie to make a blank line in between movies in Python shell
print

groundhog_day = media.Movie("Groundhog Day",
            "Man gets stuck reliving Groundhog Day over and over",
            "https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
            "https://youtu.be/tSVeDx9fk60")
print(groundhog_day.title)
print(groundhog_day.storyline)
print

kubo = media.Movie("Kubo and the Two Strings",
            "A boy's magical quest in samurai Japan",
            "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Kubo_and_the_Two_Strings_poster.png/220px-Kubo_and_the_Two_Strings_poster.png",
            "https://youtu.be/p4-6qJzeb3A")
print(kubo.title)
print(kubo.storyline)
print

like_water = media.Movie("Like Water for Chocolate",
            "A forbidden love story set in rural Mexico",
            "https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Likewaterforchocolate.PNG/220px-Likewaterforchocolate.PNG",
            "https://youtu.be/vb2QJvmETL4")
print(like_water.title)
print(like_water.storyline)
print

ghost_protocol = media.Movie("Mission Impossible: Ghost Protocol",
            "Disavowed spies strive to save the world",
            "https://upload.wikimedia.org/wikipedia/en/thumb/b/b5/Mission_impossible_ghost_protocol.jpg/220px-Mission_impossible_ghost_protocol.jpg",
            "https://youtu.be/7wkih9Yvxq0")
print(ghost_protocol.title)
print(ghost_protocol.storyline)
print

eat_drink = media.Movie("Eat Drink Man Woman",
            "Passion & modern roles of women explored, amongst great cooking",
            "https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Eat_Drink_Man_Woman.jpg/220px-Eat_Drink_Man_Woman.jpg",
            "https://youtu.be/l7pKpO8NErU")
print(eat_drink.title)
print(eat_drink.storyline)
print

#movies class is applied for each movie
movies = [sing, groundhog_day, kubo, like_water, ghost_protocol, eat_drink]
#fresh tomatoes file is applied for formatting the appearance of the web page
fresh_tomatoes.open_movies_page(movies)

