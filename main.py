"""Main entry point for the Library Management System."""

from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError,
)


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("=" * 50)


def add_book(service: LibraryService):
    """Handle add book operation."""
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        
        book = service.add_book(book_id, title, author)
        print(f"✓ Book added: {title}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def register_member(service: LibraryService):
    """Handle register member operation."""
    try:
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Member Email: ").strip()
        
        member = service.register_member(member_id, name, email)
        print(f"✓ Member registered: {name}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def borrow_book(service: LibraryService):
    """Handle borrow book operation."""
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        loan = service.borrow_book(book_id, member_id)
        print(f"✓ {loan.member.name} borrowed {loan.book.title}")
    except BookNotFoundError as e:
        print(f"✗ {e}")
    except MemberNotFoundError as e:
        print(f"✗ {e}")
    except BookUnavailableError as e:
        print(f"✗ {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def return_book(service: LibraryService):
    """Handle return book operation."""
    try:
        loan_id = input("Enter Loan ID: ").strip()
        
        loan = service.return_book(loan_id)
        print(f"✓ {loan.member.name} returned {loan.book.title}")
    except LoanNotFoundError as e:
        print(f"✗ {e}")
    except ValueError as e:
        print(f"✗ {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def view_books(service: LibraryService):
    """Display all books."""
    books = service.view_books()
    if not books:
        print("\n✓ No books found.")
        return
    
    print("\n" + "=" * 60)
    print("BOOKS:")
    print("=" * 60)
    for book in books:
        print(f"  {book}")
    print("=" * 60)


def view_members(service: LibraryService):
    """Display all members."""
    members = service.view_members()
    if not members:
        print("\n✓ No members found.")
        return
    
    print("\n" + "=" * 60)
    print("MEMBERS:")
    print("=" * 60)
    for member in members:
        print(f"  {member}")
    print("=" * 60)


def view_loans(service: LibraryService):
    """Display all loans."""
    loans = service.view_loans()
    if not loans:
        print("\n✓ No loans found.")
        return
    
    print("\n" + "=" * 60)
    print("LOANS:")
    print("=" * 60)
    for loan in loans:
        print(f"  {loan}")
    print("=" * 60)


def main():
    """Main application loop.
    
    Flowchart: Orchestrates all 8 operations
    """
    service = LibraryService()
    
    print("\n✓ Welcome to Library Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\n✓ Program closed.")
            break
        else:
            print("✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
