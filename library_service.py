"""Library Service - Core business logic for the Library Management System."""

from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError,
)
from typing import List, Dict


class LibraryService:
    """Service class for managing library operations."""

    def __init__(self):
        self._books: Dict[str, Book] = {}
        self._members: Dict[str, Member] = {}
        self._loans: List[Loan] = []
        self._loan_counter = 0

    # ==================== BOOK OPERATIONS ====================

    def add_book(self, book_id: str, title: str, author: str) -> Book:
        """Add a new book to the library.
        
        Flowchart: _01_add_book.svg
        """
        if book_id in self._books:
            raise ValueError(f"Book with ID {book_id} already exists.")
        
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book

    def view_books(self) -> List[Book]:
        """Get a list of all books in the library.
        
        Flowchart: _05_view_book.svg
        """
        return list(self._books.values())

    # ==================== MEMBER OPERATIONS ====================

    def register_member(self, member_id: str, name: str, email: str) -> Member:
        """Register a new member to the library.
        
        Flowchart: _02_register_member.svg
        """
        if member_id in self._members:
            raise ValueError(f"Member with ID {member_id} already exists.")
        
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member

    def view_members(self) -> List[Member]:
        """Get a list of all members in the library.
        
        Flowchart: _06_view_member.svg
        """
        return list(self._members.values())

    # ==================== LOAN OPERATIONS ====================

    def borrow_book(self, book_id: str, member_id: str) -> Loan:
        """Process a book borrowing request.
        
        Flowchart: _03_borrow_book.svg
        
        Validates:
        - Book exists
        - Member exists
        - Book is available
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"Book not found.")

        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member not found.")

        # Check if book is available
        if not book.available:
            raise BookUnavailableError(f"Book is already borrowed.")

        # Borrow the book
        book.borrow()

        # Create loan
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)

        return loan

    def return_book(self, loan_id: str) -> Loan:
        """Process a book return request.
        
        Flowchart: _04_return_book.svg
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break

        if loan is None:
            raise LoanNotFoundError(f"Loan not found.")

        if not loan.is_active:
            raise ValueError(f"Loan {loan_id} is already closed.")

        # Return the book
        loan.book.return_book()
        loan.close_loan()

        return loan

    def view_loans(self) -> List[Loan]:
        """Get a list of all loans.
        
        Flowchart: _07_view_loan.svg
        """
        return list(self._loans)
