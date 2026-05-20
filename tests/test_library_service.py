"""Unit tests for LibraryService."""

import unittest
from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError,
)


class TestLibraryService(unittest.TestCase):
    """Test cases for LibraryService."""

    def setUp(self):
        self.service = LibraryService()
        # Add test data
        self.service.add_book("B001", "Python Guide", "John Doe")
        self.service.add_book("B002", "Java Basics", "Jane Smith")
        self.service.register_member("M001", "Alice", "alice@example.com")
        self.service.register_member("M002", "Bob", "bob@example.com")

    # ==================== BOOK TESTS ====================

    def test_add_book(self):
        """Test adding a book."""
        book = self.service.add_book("B003", "C++ Advanced", "Tom Brown")
        self.assertEqual(book.book_id, "B003")
        self.assertTrue(book.available)

    def test_add_duplicate_book(self):
        """Test adding a duplicate book raises error."""
        with self.assertRaises(ValueError):
            self.service.add_book("B001", "Duplicate", "Author")

    def test_view_books(self):
        """Test viewing all books."""
        books = self.service.view_books()
        self.assertEqual(len(books), 2)

    def test_view_books_empty(self):
        """Test viewing books when none exist."""
        empty_service = LibraryService()
        books = empty_service.view_books()
        self.assertEqual(len(books), 0)

    # ==================== MEMBER TESTS ====================

    def test_register_member(self):
        """Test registering a member."""
        member = self.service.register_member("M003", "Charlie", "charlie@example.com")
        self.assertEqual(member.member_id, "M003")
        self.assertEqual(member.name, "Charlie")

    def test_register_duplicate_member(self):
        """Test registering duplicate member raises error."""
        with self.assertRaises(ValueError):
            self.service.register_member("M001", "Duplicate", "dup@example.com")

    def test_view_members(self):
        """Test viewing all members."""
        members = self.service.view_members()
        self.assertEqual(len(members), 2)

    def test_view_members_empty(self):
        """Test viewing members when none exist."""
        empty_service = LibraryService()
        members = empty_service.view_members()
        self.assertEqual(len(members), 0)

    # ==================== LOAN TESTS ====================

    def test_borrow_book_success(self):
        """Test successful book borrowing."""
        loan = self.service.borrow_book("B001", "M001")
        self.assertEqual(loan.loan_id, "L001")
        self.assertTrue(loan.is_active)
        # Check book is no longer available
        book = self.service._books["B001"]
        self.assertFalse(book.available)

    def test_borrow_nonexistent_book(self):
        """Test borrowing a non-existent book raises error."""
        with self.assertRaises(BookNotFoundError):
            self.service.borrow_book("B999", "M001")

    def test_borrow_nonexistent_member(self):
        """Test borrowing for non-existent member raises error."""
        with self.assertRaises(MemberNotFoundError):
            self.service.borrow_book("B001", "M999")

    def test_borrow_unavailable_book(self):
        """Test borrowing an unavailable book raises error."""
        self.service.borrow_book("B001", "M001")
        with self.assertRaises(BookUnavailableError):
            self.service.borrow_book("B001", "M002")

    def test_return_book_success(self):
        """Test successful book return."""
        loan = self.service.borrow_book("B001", "M001")
        returned_loan = self.service.return_book("L001")
        self.assertFalse(returned_loan.is_active)
        # Check book is available again
        book = self.service._books["B001"]
        self.assertTrue(book.available)

    def test_return_nonexistent_loan(self):
        """Test returning a non-existent loan raises error."""
        with self.assertRaises(LoanNotFoundError):
            self.service.return_book("L999")

    def test_return_already_closed_loan(self):
        """Test returning an already closed loan raises error."""
        loan = self.service.borrow_book("B001", "M001")
        self.service.return_book("L001")
        with self.assertRaises(ValueError):
            self.service.return_book("L001")

    def test_view_loans(self):
        """Test viewing all loans."""
        self.service.borrow_book("B001", "M001")
        self.service.borrow_book("B002", "M002")
        loans = self.service.view_loans()
        self.assertEqual(len(loans), 2)

    def test_view_loans_empty(self):
        """Test viewing loans when none exist."""
        loans = self.service.view_loans()
        self.assertEqual(len(loans), 0)

    def test_loan_id_generation(self):
        """Test loan IDs are generated correctly."""
        loan1 = self.service.borrow_book("B001", "M001")
        loan2 = self.service.borrow_book("B002", "M002")
        self.assertEqual(loan1.loan_id, "L001")
        self.assertEqual(loan2.loan_id, "L002")

    def test_multiple_borrows_and_returns(self):
        """Test multiple borrow and return operations."""
        # Borrow
        loan1 = self.service.borrow_book("B001", "M001")
        # Return
        self.service.return_book("L001")
        # Borrow again
        loan2 = self.service.borrow_book("B001", "M002")
        self.assertEqual(loan2.loan_id, "L002")
        # Check original member can't borrow same book again
        with self.assertRaises(BookUnavailableError):
            self.service.borrow_book("B001", "M001")


if __name__ == "__main__":
    unittest.main()
