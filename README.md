# Library Management System

A comprehensive Python-based library management system featuring book inventory, member registration, and loan tracking capabilities.

## Features

### ✅ Core Operations

1. **Add Book** - Register new books with availability tracking
2. **Register Member** - Add library members with contact information
3. **Borrow Book** - Process borrowing requests with automatic validation
4. **Return Book** - Process book returns and close loan transactions
5. **View Books** - Display all books with their availability status
6. **View Members** - Display all registered library members
7. **View Loans** - Display all active and closed loans
8. **Exit** - Gracefully close the application

## System Architecture

### Files

- **main.py** - Interactive CLI application entry point
- **models.py** - Data models (Book, Member, Loan)
- **library_service.py** - Core business logic and service layer
- **exceptions.py** - Custom exception classes for error handling
- **tests/** - Comprehensive unit test suite

## Data Models

### Book
```python
Book(book_id, title, author)
- book_id: Unique identifier
- title: Book title
- author: Book author
- available: Availability status (default: True)
```

### Member
```python
Member(member_id, name, email)
- member_id: Unique identifier
- name: Member's full name
- email: Contact email
```

### Loan
```python
Loan(loan_id, book, member)
- loan_id: Unique identifier (auto-generated: L001, L002, etc.)
- book: Reference to Book object
- member: Reference to Member object
- borrow_date: Date/time of borrowing
- return_date: Date/time of return (None if active)
- is_active: Loan status (True = active, False = closed)
```

## Error Handling

The system includes custom exceptions for different error scenarios:

- **BookNotFoundError** - Book ID not found in inventory
- **MemberNotFoundError** - Member ID not found in registry
- **BookUnavailableError** - Book is already borrowed
- **LoanNotFoundError** - Loan ID not found
- **InvalidInputError** - Invalid user input

## Usage

### Installation

No external dependencies required. Uses Python standard library only.

```bash
pip install -r requirements.txt  # Optional, for documentation
```

### Running the Application

```bash
python main.py
```

This launches an interactive menu-driven CLI interface.

### Running Tests

```bash
# Run all tests
python -m unittest discover tests/

# Run specific test file
python -m unittest tests.test_models
python -m unittest tests.test_library_service

# Run with verbose output
python -m unittest discover tests/ -v
```

## Example Workflow

```
1. Add Book
   - Book ID: B001
   - Title: Python Guide
   - Author: John Doe
   ✓ Book added: Python Guide

2. Register Member
   - Member ID: M001
   - Name: Alice
   - Email: alice@example.com
   ✓ Member registered: Alice

3. Borrow Book
   - Book ID: B001
   - Member ID: M001
   ✓ Alice borrowed Python Guide

4. View Loans
   - L001 - Alice borrowed Python Guide [Active]

5. Return Book
   - Loan ID: L001
   ✓ Alice returned Python Guide

6. View Loans
   - L001 - Alice borrowed Python Guide [Closed]
```

## Testing

The project includes comprehensive unit tests:

- **test_models.py** - Tests for Book, Member, and Loan models
- **test_library_service.py** - Tests for LibraryService operations

Total: 26 test cases covering all functionality and error scenarios.

## Design Patterns

- **Service Layer** - Business logic separated from UI
- **Model Layer** - Data representation with methods
- **Exception Handling** - Custom exceptions for specific error cases
- **Dictionary Storage** - Efficient O(1) lookup for books and members
- **List Storage** - Simple loan tracking with sequential IDs

## Future Enhancements

- Persistent data storage (database/file)
- Book reservations
- Late fee calculations
- Member search and filtering
- Book search and filtering
- Due date reminders
- Multi-copy books support
- Ratings and reviews

## License

Open source - Free to use and modify.
