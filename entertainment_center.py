# Instances of class movie with some of my favourite movies


import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=2BlMNH1QTeE",
                        "John Lasseter",
                        "https://en.wikipedia.org/wiki/Toy_Story")

lord_of_the_rings = media.Movie("Lord Of The Rings",
                                "The Lord of the Rings is a film series \
                                consisting of three epic fantasy adventure \
                                films.",
                                "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",  # noqa
                                "https://www.youtube.com/watch?v=aStYWD25fAQ",
                                "Peter Jackson",
                                "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings")  # noqa

star_wars = media.Movie("Star Wars - The Force Awaken",
                        "The force rise again",
                        "http://i2.wp.com/bitcast-a-sm.bitgravity.com/slashfilm/wp/wp-content/images/star-wars-7-struzan-poster-full.jpg",  # noqa
                        "https://www.youtube.com/watch?v=ngElkyQ6Rhs",
                        "J.J. Abrams",
                        "https://en.wikipedia.org/wiki/Star_Wars")

t_warriors = media.Movie("The Warriors",
                         "In it, a New York City gang must return to their home\
                         turf after they are framed for the murder of a \
                         respected gang leader.",
                         "https://upload.wikimedia.org/wikipedia/en/0/03/TheWarriors_1979_Movie_Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=4GxSwUcm_XE",
                         "John Lasseter",
                         "https://en.wikipedia.org/wiki/The_Warriors_%28film%29")  # noqa

school_of_rock = media.Movie("School of Rock",
                             "Using to learn rock at school",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=5afGGGsxvEA",
                             "Richard Linklater",
                             "https://en.wikipedia.org/wiki/School_of_Rock")

conan = media.Movie("Conan the Barbarian",
                    "It is based on stories by Robert E. Howard, \
                    a pulp fiction writer of the 1930s, about the adventures\
                    of the eponymous character in a fictional pre-historic \
                    world of dark magic and savagery.",
                    "https://upload.wikimedia.org/wikipedia/en/8/81/Conan_the_Barbarian_by_Renato_Casaro.jpg",  # noqa
                    "https://www.youtube.com/watch?v=Y0cxNbz4yKc",
                    "John Milius",
                    "https://en.wikipedia.org/wiki/Conan_the_Barbarian_%281982_film%29")  # noqa

movies = [toy_story, lord_of_the_rings,
          star_wars, t_warriors,
          school_of_rock, conan]

fresh_tomatoes.open_movies_page(movies)
