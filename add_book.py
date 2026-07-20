def add_book(books):
    title = input("Введіть назву книги: ")
    author = input("Введіть автора книги: ")
    book = {
            "title": title,
            "author": author,
            "status": "unread",
        }
    books.append(book)
    print("Книга додана до списку")

books = []
add_book(books)
print(books)