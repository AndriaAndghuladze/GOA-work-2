from django.shortcuts import render

# Create your views here.
movies_database = [
    {"id": 0, "title": "Interstellar", "year": 2014, "rating": 8.7},
    {"id": 1, "title": "The Shawshank Redemption", "year": 1994, "rating": 9.3},
    {"id": 2, "title": "The Godfather", "year": 1972, "rating": 9.2},
    {"id": 3, "title": "The Dark Knight", "year": 2008, "rating": 9.0},
    {"id": 4, "title": "Pulp Fiction", "year": 1994, "rating": 8.9},
    {"id": 5, "title": "Inception", "year": 2010, "rating": 8.8},
    {"id": 6, "title": "Fight Club", "year": 1999, "rating": 8.8},
    {"id": 7, "title": "Forrest Gump", "year": 1994, "rating": 8.8},
    {"id": 8, "title": "The Matrix", "year": 1999, "rating": 8.7},
    {"id": 9, "title": "Goodfellas", "year": 1990, "rating": 8.7},
    {"id": 10, "title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001, "rating": 8.8},
    {"id": 11, "title": "Star Wars: Episode V - The Empire Strikes Back", "year": 1980, "rating": 8.7},
    {"id": 12, "title": "Spirited Away", "year": 2001, "rating": 8.6},
    {"id": 13, "title": "Saving Private Ryan", "year": 1998, "rating": 8.6},
    {"id": 14, "title": "The Green Mile", "year": 1999, "rating": 8.6},
    {"id": 15, "title": "Gladiator", "year": 2000, "rating": 8.5},
    {"id": 16, "title": "The Departed", "year": 2006, "rating": 8.5},
    {"id": 17, "title": "The Prestige", "year": 2006, "rating": 8.5},
    {"id": 18, "title": "Whiplash", "year": 2014, "rating": 8.5},
    {"id": 19, "title": "The Lion King", "year": 1994, "rating": 8.5},
    {"id": 20, "title": "Parasite", "year": 2019, "rating": 8.5},
    {"id": 21, "title": "Memento", "year": 2000, "rating": 8.4},
    {"id": 22, "title": "The Pianist", "year": 2002, "rating": 8.5},
    {"id": 23, "title": "Django Unchained", "year": 2012, "rating": 8.5},
    {"id": 24, "title": "The Shining", "year": 1980, "rating": 8.4},
    {"id": 25, "title": "WALL-E", "year": 2008, "rating": 8.4},
    {"id": 26, "title": "Joker", "year": 2019, "rating": 8.4},
    {"id": 27, "title": "Spider-Man: Into the Spider-Verse", "year": 2018, "rating": 8.4},
    {"id": 28, "title": "Oldboy", "year": 2003, "rating": 8.3},
    {"id": 29, "title": "Inglourious Basterds", "year": 2009, "rating": 8.3}
]

def all_movies(request):
    return render(request, 'movies/main.html', {'movies': movies_database})

def movie_detail(request, movie_id):
    selected_movie = None
 
    for movie in movies_database:
        if movie['id'] == movie_id:
            selected_movie = movie  
            break

    return render(request, 'movies/info.html', {'movie': selected_movie})