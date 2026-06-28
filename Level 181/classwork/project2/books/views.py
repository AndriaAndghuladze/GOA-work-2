from django.shortcuts import render

# Create your views here.
books_database = [
    {"id": 0, "title": "Harry Potter and the Philosopher's Stone", "author": "J. K. Rowling", "pages": 320},
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien", "pages": 310},
    {"id": 2, "title": "1984", "author": "George Orwell", "pages": 328},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 281},
    {"id": 4, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J. D. Salinger", "pages": 234},
    {"id": 6, "title": "Pride and Prejudice", "author": "Jane Austen", "pages": 279},
    {"id": 7, "title": "The Fellowship of the Ring", "author": "J. R. R. Tolkien", "pages": 423},
    {"id": 8, "title": "Animal Farm", "author": "George Orwell", "pages": 141},
    {"id": 9, "title": "Brave New World", "author": "Aldous Huxley", "pages": 268},
    {"id": 10, "title": "The Book Thief", "author": "Markus Zusak", "pages": 552},
    {"id": 11, "title": "The Alchemist", "author": "Paulo Coelho", "pages": 208},
    {"id": 12, "title": "Fahrenheit 451", "author": "Ray Bradbury", "pages": 158},
    {"id": 13, "title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "pages": 96},
    {"id": 14, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "pages": 671},
    {"id": 15, "title": "The Chronicles of Narnia", "author": "C. S. Lewis", "pages": 767},
    {"id": 16, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "pages": 254},
    {"id": 17, "title": "Frankenstein", "author": "Mary Shelley", "pages": 280},
    {"id": 18, "title": "Dracula", "author": "Bram Stoker", "pages": 418},
    {"id": 19, "title": "The Kite Runner", "author": "Khaled Hosseini", "pages": 371},
    {"id": 20, "title": "Catch-22", "author": "Joseph Heller", "pages": 453},
    {"id": 21, "title": "Sapiens", "author": "Yuval Noah Harari", "pages": 512},
    {"id": 22, "title": "Dune", "author": "Frank Herbert", "pages": 604},
    {"id": 23, "title": "The Road", "author": "Cormac McCarthy", "pages": 287},
    {"id": 24, "title": "Life of Pi", "author": "Yann Martel", "pages": 319},
    {"id": 25, "title": "The Da Vinci Code", "author": "Dan Brown", "pages": 454},
    {"id": 26, "title": "Gone Girl", "author": "Gillian Flynn", "pages": 415},
    {"id": 27, "title": "The Hunger Games", "author": "Suzanne Collins", "pages": 374},
    {"id": 28, "title": "The Fault in Our Stars", "author": "John Green", "pages": 313},
    {"id": 29, "title": "Lord of the Flies", "author": "William Golding", "pages": 182}
]

def all_books(request):
    return render(request, 'books/main.html', {'books': books_database})

def book_detail(request, book_id):
    selected_book = None
 
    for book in books_database:
        if book['id'] == book_id:
            selected_book = book  
            break

    return render(request, 'books/info.html', {'book': selected_book})