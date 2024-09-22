library_data = {
    "library": {
        "books": [
            {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "genres": ["Novel", "Historical"],
                "available": True
            },
            {
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "year": 1960,
                "genres": ["Novel", "Southern Gothic", "Bildungsroman"],
                "available": False
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "genres": ["Dystopian", "Science Fiction"],
                "available": True
            },
            {
                "title": "Moby-Dick",
                "author": "Herman Melville",
                "year": 1851,
                "genres": ["Novel", "Adventure"],
                "available": False
            }
        ]
    }
}

available_books = [book for book in library_data['library']['books'] if book['available']]

unique_authors = list({book['author'] for book in library_data['library']['books']})

result = {
    "available_books": available_books,
    "unique_authors": unique_authors
}

import json
print(json.dumps(result, indent=4))