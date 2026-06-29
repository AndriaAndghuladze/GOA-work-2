from django.shortcuts import render

# Create your views here.
movies_database = [
    {"id": 0, "title": "Inception", "director": "Christopher Nolan", "year": 2010},
    {"id": 1, "title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008},
    {"id": 2, "title": "Interstellar", "director": "Christopher Nolan", "year": 2014},
    {"id": 3, "title": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994},
    {"id": 4, "title": "Inglourious Basterds", "director": "Quentin Tarantino", "year": 2009},
    {"id": 5, "title": "Django Unchained", "director": "Quentin Tarantino", "year": 2012},
    {"id": 6, "title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994},
    {"id": 7, "title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972},
    {"id": 8, "title": "The Godfather Part II", "director": "Francis Ford Coppola", "year": 1974},
    {"id": 9, "title": "Fight Club", "director": "David Fincher", "year": 1999},
    {"id": 10, "title": "Se7en", "director": "David Fincher", "year": 1995},
    {"id": 11, "title": "The Social Network", "director": "David Fincher", "year": 2010},
    {"id": 12, "title": "Forrest Gump", "director": "Robert Zemeckis", "year": 1994},
    {"id": 13, "title": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "year": 1999},
    {"id": 14, "title": "Goodfellas", "director": "Martin Scorsese", "year": 1990},
    {"id": 15, "title": "The Departed", "director": "Martin Scorsese", "year": 2006},
    {"id": 16, "title": "The Wolf of Wall Street", "director": "Martin Scorsese", "year": 2013},
    {"id": 17, "title": "Schindler's List", "director": "Steven Spielberg", "year": 1993},
    {"id": 18, "title": "Saving Private Ryan", "director": "Steven Spielberg", "year": 1998},
    {"id": 19, "title": "Jurassic Park", "director": "Steven Spielberg", "year": 1993},
    {"id": 20, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "year": 2001},
    {"id": 21, "title": "The Lord of the Rings: The Two Towers", "director": "Peter Jackson", "year": 2002},
    {"id": 22, "title": "The Lord of the Rings: The Return of the King", "director": "Peter Jackson", "year": 2003},
    {"id": 23, "title": "Gladiator", "director": "Ridley Scott", "year": 2000},
    {"id": 24, "title": "Alien", "director": "Ridley Scott", "year": 1979},
    {"id": 25, "title": "Blade Runner 2049", "director": "Denis Villeneuve", "year": 2017},
    {"id": 26, "title": "Dune", "director": "Denis Villeneuve", "year": 2021},
    {"id": 27, "title": "Whiplash", "director": "Damien Chazelle", "year": 2014},
    {"id": 28, "title": "La La Land", "director": "Damien Chazelle", "year": 2016},
    {"id": 29, "title": "Parasite", "director": "Bong Joon Ho", "year": 2019}
]


def index(request):
    return render(request, 'movies/index.html')

def movie_list(request):
    context = {'movies': movies_database}
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):    

    movie = next((movie for movie in movies_database if movie["id"] == movie_id), None)
    if movie is None:
        return render(request, 'movies/movie_not_found.html', status=404)
    context = {'movie': movie}
    return render(request, 'movies/movie_detail.html', context)