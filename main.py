# from abc import ABC, abstractmethod


def count_vowels(text):
    count = int(0)
    if type(text) is not str:
        return int(42)
    else:
        for i in text:
            if i in "aeiouAEIOU":
                count += 1
    return int(count)


def hamming(text1, text2):
    if len(text1) != len(text2):
        print("Awww... too bad :( The lengths of the strings are not equal")
        return 0
    else:
        return len([i for i in filter(lambda x: x[0] != x[1], zip(text1, text2))])


# class Vehicle(ABC):
class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    # @abstractmethod
    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        print(f"Hello user! I'm a {self.color} car that's equipped with {self.doors} doors. "
              f"Please fuel me with {self.fuel_type} only! Thank you :)")
        return "Color: {}, Fuel Type: {}, Doors: {}".format(self.color, self.fuel_type, self.doors)


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        print(f"Hello user! I'm a {self.color} bus that can carry up to {self.passengers} passengers. "
              f"Please fuel me with {self.fuel_type} only! Thank you :)")
        return "Color: {}, Fuel Type: {}, Passengers: {}".format(self.color, self.fuel_type, self.passengers)


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "{}, {}".format(self.name, self.author)

    # def __repr__(self):
        # return str(self)


class BookShelf:

    def __init__(self):
        self.books = []

    def add_book_list(self, books):
        self.books.extend([book for book in set(books) if isinstance(book, Book)])

    def book_by_author(self, author):
        return [book.name for book in self.books if book.author == author]

    def get_books(self):
        return [book.name for book in self.books]

    def clear_shelf(self):
        self.books.clear()
