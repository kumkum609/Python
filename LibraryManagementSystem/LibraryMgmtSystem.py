#Library Management System
#List to store all available books in the library
Book_list =[
    {
     "Bookname": "Math",
     "Author name": "RD Sharma",
     "Published in": 2022,
     "Book_id": "M22"
        },
        {
     "Bookname": "English",
     "Author name": "Alice",
     "Published in": 2019,
     "Book_id": "M19"
        },
        {
     "Bookname": "Clean code",
     "Author name": "Robert C.Martin",
     "Published in": 2008,
     "Book_id": "B102"
        },
        {
     "Bookname": "Atomic Habits",
     "Author name": "James Clear",
     "Published in": 2018,
     "Book_id": "B103"
        }]
#Functions to display all available books
def view_book():
    print("Available books are:")
    for books in Book_list:
        print(f"Book Name: {books['Bookname']}")
        print(f"Author name: {books['Author name']}")
        print(f"Published in: {books['Published in']}")
        print(f"Book id: {books['Book_id']}")
        print("-"*30)

#Function to borrow a book from the library
Borrowed_list =[]
def borrow_book():
    print("Enter book name you want to borrow: ")
    book_name =input().strip().title()
    for books in Book_list:
        if books["Bookname"].title() ==book_name:
            print(f"You borrowed {books['Bookname']} book!")
            Borrowed_list.append(books) #add in borrow list
            Book_list.remove(books) #remove the borrowed book from available book

            print("-"*30)
            view_book()
            return
    print("Not available!")

#Function to return a book
def return_book():
    print("Do you want to return book? :Yes or No ")
    user_input = input().strip().title()
    if user_input=='Yes':
        print("Enter the name of book you want to return:")
        user_return=input().strip().title()
        for books in Borrowed_list:
                    if books["Bookname"].title() ==user_return:
                         Book_list.append(books) #add the returned book back to the library
                         Borrowed_list.remove(books)
                         print(f"You returned {books['Bookname']} book")
                         print("-"*30)
                         view_book()
                         return
                
        print("This book is not borrowed!")       
    else:
        print("Return Cancelled!")

#add the new book to the library
def add_book():
    print("Do you want to add the book in this library? :Yes or No")
    user_inp =input().strip().capitalize()
    if user_inp=='Yes':
        print("----Enter the details----")
        print("Enter Book name:",end=" ")
        B_name = input().strip().title()
        print("Enter author name:",end=" ")
        Author_name =input().strip().title()
        print("Book Published in:",end=" ")
        publish_in = int(input().strip())
        print("Enter book id:",end=" ")
        B_id =input().strip()
        print("-"*30)
        new_Book= {
            "Bookname": B_name,
            "Author name": Author_name,
            "Published in": publish_in,
            "Book_id": B_id
            }
        
        Book_list.append(new_Book)
       # print(f"{new_Book} added!")
        print(f"Book Name: {new_Book['Bookname']}")
        print(f"Author name: {new_Book['Author name']}")
        print(f"Published in: {new_Book['Published in']}")
        print(f"Book id: {new_Book['Book_id']}")
       
        print("New book added Successfully!")
        print("-"*30)

    else:
        print("No book added!")
def show_menu():
    print("Library Mangaement System ")
    print("1. View Book\n2. Borrow Book\n3. Return Book\n4. Add book\n5. Exit")
    print("-"*30)
def library():
    while True:
        show_menu()
        print("Enter your choice: ")
        choice = int(input())
    #while True:
        if choice==1:
            view_book()
        elif choice==2:
            borrow_book()
        elif choice==3:
            return_book()
        elif choice==4:
            add_book()
        elif choice==5:
            print("Thank you for using Library Management System!")
            print("Exit")
            break
        else:
            print("Invalid choice! Please try again")
library()