import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room. ",
                        "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

#print(avatar.storyline)

serial_mom = media.Movie("Serial Mom",
                         "A sweet mother finds herself participating in homicidal activities when she sees the occasion call for it.",
                         "https://m.media-amazon.com/images/M/MV5BYjM0N2ViMzUtMTc1OS00YmEzLWE2NWYtNjU5NTY4NjRlOTI0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,670,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=Ut9GvlhB9f4")



school_of_rock = media.Movie("School of Rock",
                             "After being kicked out of his rock band, Dewey Finn becomes a substitute teacher of an uptight elementary private school, only to try and turn them into a rock band.",
                             "https://m.media-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg",
                             "https://www.youtube.com/watch?v=4AeUHwkIJzU")

#school_of_rock.show_trailer()

the_little_death = media.Movie("The Little Death",
                               "The secret lives of five suburban couples living in Sydney reveal both the fetishes and the repercussions that come with sharing them.",
                               "https://m.media-amazon.com/images/M/MV5BMTgzOTM0OTIyMV5BMl5BanBnXkFtZTgwNzk0NDMzMjE@._V1_SY1000_CR0,0,693,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=V1TClqjaKsg")

ex_machina = media.Movie("Ex Machina",
                         "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a highly advanced humanoid A.I.",
                         "https://m.media-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=bggUmgeMCdc")

movies = [toy_story, avatar, serial_mom, school_of_rock, the_little_death, ex_machina]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__module__)
