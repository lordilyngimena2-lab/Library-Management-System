"""Custom exceptions for the Library Management System."""


class BookNotFoundError(Exception):
    """Raised when a book with the given ID is not found."""
    pass


class MemberNotFoundError(Exception):
    """Raised when a member with the given ID is not found."""
    pass


class BookUnavailableError(Exception):
    """Raised when a book is not available for borrowing."""
    pass


class LoanNotFoundError(Exception):
    """Raised when a loan with the given ID is not found."""
    pass


class InvalidInputError(Exception):
    """Raised when invalid input is provided."""
    pass
