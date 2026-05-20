"""Unit tests for models."""

import unittest
from models import Book, Member, Loan
from datetime import datetime


class TestBook(unittest.TestCase):
    """Test cases for Book model."""

    def setUp(self):
        self.book = Book("B001", "Python Guide", "John Doe")

    def test_book_creation(self):
        """Test book creation."""
        self.assertEqual(self.book.book_id, "B001")
        self.assertEqual(self.book.title, "Python Guide")
        self.assertEqual(self.book.author, "John Doe")
        self.assertTrue(self.book.available)

    def test_book_borrow(self):
        """Test borrowing a book."""
        self.book.borrow()
        self.assertFalse(self.book.available)

    def test_book_borrow_unavailable(self):
        """Test borrowing an unavailable book raises error."""
        self.book.borrow()
        with self.assertRaises(ValueError):
            self.book.borrow()

    def test_book_return(self):
        """Test returning a book."""
        self.book.borrow()
        self.book.return_book()
        self.assertTrue(self.book.available)

    def test_book_return_not_borrowed(self):
        """Test returning a non-borrowed book raises error."""
        with self.assertRaises(ValueError):
            self.book.return_book()

    def test_book_str(self):
        """Test book string representation."""
        expected = "B001 - Python Guide by John Doe [Available]"
        self.assertEqual(str(self.book), expected)

    def test_book_str_borrowed(self):
        """Test book string representation when borrowed."""
        self.book.borrow()
        expected = "B001 - Python Guide by John Doe [Borrowed]"
        self.assertEqual(str(self.book), expected)


class TestMember(unittest.TestCase):
    """Test cases for Member model."""

    def setUp(self):
        self.member = Member("M001", "Alice", "alice@example.com")

    def test_member_creation(self):
        """Test member creation."""
        self.assertEqual(self.member.member_id, "M001")
        self.assertEqual(self.member.name, "Alice")
        self.assertEqual(self.member.email, "alice@example.com")

    def test_member_str(self):
        """Test member string representation."""
        expected = "M001 - Alice (alice@example.com)"
        self.assertEqual(str(self.member), expected)


class TestLoan(unittest.TestCase):
    """Test cases for Loan model."""

    def setUp(self):
        self.book = Book("B001", "Python Guide", "John Doe")
        self.member = Member("M001", "Alice", "alice@example.com")
        self.loan = Loan("L001", self.book, self.member)

    def test_loan_creation(self):
        """Test loan creation."""
        self.assertEqual(self.loan.loan_id, "L001")
        self.assertEqual(self.loan.book, self.book)
        self.assertEqual(self.loan.member, self.member)
        self.assertTrue(self.loan.is_active)
        self.assertIsNone(self.loan.return_date)

    def test_loan_close(self):
        """Test closing a loan."""
        self.loan.close_loan()
        self.assertFalse(self.loan.is_active)
        self.assertIsNotNone(self.loan.return_date)

    def test_loan_close_already_closed(self):
        """Test closing an already closed loan raises error."""
        self.loan.close_loan()
        with self.assertRaises(ValueError):
            self.loan.close_loan()

    def test_loan_str(self):
        """Test loan string representation."""
        expected = "L001 - Alice borrowed Python Guide [Active]"
        self.assertEqual(str(self.loan), expected)

    def test_loan_str_closed(self):
        """Test loan string representation when closed."""
        self.loan.close_loan()
        expected = "L001 - Alice borrowed Python Guide [Closed]"
        self.assertEqual(str(self.loan), expected)


if __name__ == "__main__":
    unittest.main()
