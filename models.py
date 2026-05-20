from datetime import datetime
from typing import Optional

class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        """Mark book as borrowed."""
        if not self.available:
            raise ValueError(f"Book '{self.title}' is already borrowed.")
        self.available = False
    
    def return_book(self):
        """Mark book as returned."""
        if self.available:
            raise ValueError(f"Book '{self.title}' is not borrowed.")
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"


class Member:
    """Represents a library member."""
    
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"{self.member_id} - {self.name} ({self.email})"


class Loan:
    """Represents a book loan transaction."""
    
    def __init__(self, loan_id: str, book: Book, member: Member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.borrow_date = datetime.now()
        self.return_date: Optional[datetime] = None
        self.is_active = True
    
    def close_loan(self):
        """Close the loan transaction."""
        if not self.is_active:
            raise ValueError(f"Loan {self.loan_id} is already closed.")
        self.return_date = datetime.now()
        self.is_active = False
    
    def __str__(self):
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
