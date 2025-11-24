"""
Enunciado:
Desarrolla un sistema de gestión de préstamos de libros en una biblioteca utilizando Python, el cual permite registrar
préstamos y devoluciones, además de mantener un registro de la popularidad de los libros mediante el uso de colecciones
avanzadas en Python, como `namedtuple`, `defaultdict` y `Counter`.

Funciones a desarrollar:
- define_types() -> Tuple[namedtuple, namedtuple]:
    Descripción:
    Define y retorna los tipos Book y User utilizando namedtuple, donde Book incluye los campos title, author y isbn, y
    User incluye name y email.
    
- register_loan(user: User, book: Book) -> bool:
    Descripción:
    Registra el préstamo de un libro a un usuario, actualizando los registros de préstamos y aumentando la popularidad
    del libro. Retorna True para indicar que el préstamo se registró exitosamente.
    Parámetros:
        - user (User): El usuario que realiza el préstamo.
        - book (Book): El libro que se presta.
    
- register_return(user: User, book: Book) -> bool:
    Descripción:
    Registra la devolución de un libro por parte de un usuario. Si el libro está en la lista de préstamos del usuario,
    se remueve y se retorna True. Si el libro no está en la lista, se retorna False.
    Parámetros:
        - user (User): El usuario que devuelve el libro.
        - book (Book): El libro que se devuelve.
    
- most_popular_books(N: int = 3) -> List[Tuple[Book, int]]:
    Descripción:
    Retorna una lista de los N libros más populares y la cantidad de veces que fueron prestados, utilizando Counter
    para determinar la popularidad.

Ejemplo:
    Book, User = define_types()
    loans: Dict[User, List[Book]] = defaultdict(list)
    popularity: Counter = Counter()

Salida esperada:
- Registro exitoso de préstamos y devoluciones, y una lista de los libros más populares basada en la frecuencia de
préstamos.
"""


from collections import namedtuple, defaultdict, Counter
from typing import Tuple, Dict, List, Type


def define_types() -> Tuple[Type[namedtuple], Type[namedtuple]]:
    Book = namedtuple("Book", ["title", "author", "isbn"])
    User = namedtuple("User", ["name", "email"])
    return Book, User


def register_loan(loans: dict[Type[namedtuple], list[Type[namedtuple]]], popularity: Counter, user: Type[namedtuple], book: Type[namedtuple]) -> bool:
    loans[user].append(book)
    popularity[book] += 1
    return True


def register_return(loans: dict[Type[namedtuple], list[Type[namedtuple]]], user: Type[namedtuple], book: Type[namedtuple]) -> bool:
    if book in loans[user]:
        loans[user].remove(book)
        return True
    return False


def most_popular_books(popularity: Counter, N: int = 3) -> List[Tuple[namedtuple, int]]:
    return popularity.most_common(N)


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":

    Book, User = define_types()
    loans: Dict[User, List[Book]] = defaultdict(list)
    popularity: Counter = Counter()
    
    user1 = User(name="John Doe", email="john@example.com")
    user2 = User(name="Jane Smith", email="jane@example.com")
    
    book1 = Book(title="Python 101", author="Someone", isbn="1234567890")
    book2 = Book(title="Learn Python", author="Another One", isbn="0987654321")
    book3 = Book(title="Advanced Python", author="Expert Author", isbn="1122334455")
    book4 = Book(title="Python Data Science", author="Data Scientist", isbn="2233445566")

    register_loan(loans, popularity, user1, book1)
    register_loan(loans, popularity, user2, book1)
    register_loan(loans, popularity, user2, book3)
    register_loan(loans, popularity, user1, book4)
    
    register_return(loans, user1, book4)
    
    for user, books in loans.items():
        book_titles = [book.title for book in books]
        print(f"{user.name} has borrowed: {book_titles}")
    
    popular_books = most_popular_books(popularity, 2)
    print("Most popular books based on loans:", [(book.title, count) for book, count in popular_books])
