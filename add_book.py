def add_book(books):
    title = input("Введіть назву книги: ")
    author = input("Введіть автора книги: ")
    book = {
            "title": title,
            "author": author,
            "status": "reading",
        }
    books.append(book)
    print("Книга додана до списку")