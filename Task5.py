#Task - 5 Tuple & Set
def manage_library():
    books = (
        ("To Kill a Mockingbird", "Harper Lee", 1960),
        ("1984", "George Orwell", 1949),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    )
    tags = {"classic", "dystopian", "novel", "literature"}

    print("Author of Second Book:", books[1][1])

    books = books + (("Brave New World", "Aldous Huxley", 1932),)

    title, author, year = books[2]
    print(f"Title: {title}, Author: {author}, Year: {year}")

    print("Book Titles:")
    for book in books:
        print(book[0])

    tags.add("sci-fi")
    print("\nUpdated Tags:", tags)

    tags.discard("novel")
    print("Tags after removing 'novel':", tags)

manage_library()