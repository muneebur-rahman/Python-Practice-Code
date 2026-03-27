class Book:
    def __init__(self, book_id, name):
        self.book_id = book_id
        self.name = name
        self.is_issued = False


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, name):
        self.books.append(Book(book_id, name))
        print("Book added!")

    def display_books(self):
        if not self.books:
            print("No books available!")
        for b in self.books:
            print(f"ID: {b.book_id}, Name: {b.name}, Issued: {b.is_issued}")

    def issue_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id and not b.is_issued:
                b.is_issued = True
                print("Book issued!")
                return
        print("Book not available!")

    def return_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id and b.is_issued:
                b.is_issued = False
                print("Book returned!")
                return
        print("Invalid book ID!")


# Main Menu
lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        lib.add_book(book_id, name)

    elif choice == 2:
        lib.display_books()

    elif choice == 3:
        book_id = int(input("Enter Book ID to issue: "))
        lib.issue_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID to return: "))
        lib.return_book(book_id)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")