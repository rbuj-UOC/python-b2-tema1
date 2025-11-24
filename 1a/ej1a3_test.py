import pytest
from collections import namedtuple, defaultdict, Counter
from ej1a3 import define_types, register_loan, register_return, most_popular_books

Book, User = define_types()

@pytest.fixture
def setup_library():
    """Fixture para configurar el estado inicial de la biblioteca antes de cada prueba."""
    loans = defaultdict(list)
    popularity = Counter()
    return loans, popularity

def test_register_loan(setup_library):
    loans, popularity = setup_library
    user = User(name="Alice Wonderland", email="alice@example.com")
    book = Book(title="Python for Beginners", author="Guido van Rossum", isbn="111222333")
    assert register_loan(loans, popularity, user, book) == True, "Loan registration should be successful"
    assert book in loans[user], "The book should be in the user's loan list"

def test_register_return(setup_library):
    loans, popularity = setup_library
    user = User(name="Alice Wonderland", email="alice@example.com")
    book = Book(title="Python for Beginners", author="Guido van Rossum", isbn="111222333")
    register_loan(loans, popularity, user, book)
    assert register_return(loans, user, book) == True, "Return registration should be successful"
    assert book not in loans[user], "The book should not be in the user's loan list after return"

def test_most_popular_books(setup_library):
    loans, popularity = setup_library
    user = User(name="Alice Wonderland", email="alice@example.com")
    book1 = Book(title="Python for Beginners", author="Guido van Rossum", isbn="111222333")
    book2 = Book(title="Advanced Python", author="Raymond Hettinger", isbn="444555666")
    register_loan(loans, popularity, user, book1)
    register_loan(loans, popularity, user, book2)
    register_loan(loans, popularity, user, book1)
    popular_books = most_popular_books(popularity, 1)
    assert popular_books[0][0] == book1, "The most popular book should be 'Python for Beginners'"
    assert popular_books[0][1] == 2, "'Python for Beginners' should have been loaned out twice"
