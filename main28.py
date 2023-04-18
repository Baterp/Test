#Задание 1
#Реализуйте класс «Автомобиль». Необходимо хранить
#в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
#методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

#class Car:
#    def __init__(self):
#        self.model = ''
#        self.year = 0
#        self.manufacturer = ''
#        self.engine_volume = 0.0
#        self.color = ''
#        self.price = 0.0
#    def set_model(self, model):
#        self.model = model
#    def set_year(self, year):
#        self.year = year
#    def set_manufacturer(self, manufacturer):
#        self.manufacturer = manufacturer
#    def set_engine_volume(self, engine_volume):
#        self.engine_volume = engine_volume
#    def set_color(self, color):
#        self.color = color
#    def set_price(self, price):
#        self.price = price
#    def get_model(self):
#        return self.model
#    def get_year(self):
#        return self.year
#    def get_manufacturer(self):
#        return self.manufacturer
#    def get_engine_volume(self):
#        return self.engine_volume
#    def get_color(self):
#        return self.color
#    def get_price(self):
#        return self.price
#    def input_data(self):
#        self.model = input("Введите модель автомобиля: ")
#        self.year = int(input("Введите год выпуска: "))
#        self.manufacturer = input("Введите производителя: ")
#        self.engine_volume = float(input("Введите объем двигателя: "))
#        self.color = input("Введите цвет машины: ")
#        self.price = float(input("Введите цену: "))
#    def print_data(self):
#        print("Модель автомобиля:", self.model)
#        print("Год выпуска:", self.year)
#        print("Производитель:", self.manufacturer)
#        print("Объем двигателя:", self.engine_volume)
#        print("Цвет машины:", self.color)
#        print("Цена:", self.price)
#car = Car()
#car.input_data()
#car.print_data()
#print("Модель автомобиля:", car.get_model())
#print("Год выпуска:", car.get_year())
#print("Производитель:", car.get_manufacturer())
#print("Объем двигателя:", car.get_engine_volume())
#print("Цвет машины:", car.get_color())
#print("Цена:", car.get_price())


#Задание 2
#Реализуйте класс «Книга». Необходимо хранить в
#полях класса: название книги, год выпуска, издателя,
#жанр, автора, цену. Реализуйте методы класса для ввода
#данных, вывода данных, реализуйте доступ к отдельным
#полям через методы класса.

#class Book:
#    def __init__(self, title, year, publisher, genre, author, price):
#        self.title = title
#        self.year = year
#        self.publisher = publisher
#        self.genre = genre
#        self.author = author
#        self.price = price

#    def get_title(self):
#        return self.title

#    def set_title(self, title):
#        self.title = title

#   def get_year(self):
#        return self.year

#    def set_year(self, year):
#        self.year = year

#    def get_publisher(self):
#        return self.publisher

#    def set_publisher(self, publisher):
#        self.publisher = publisher

#    def get_genre(self):
#        return self.genre

#    def set_genre(self, genre):
#        self.genre = genre

#    def get_author(self):
#        return self.author

#    def set_author(self, author):
#        self.author = author

#   def get_price(self):
#        return self.price

#    def set_price(self, price):
#        self.price = price

#    def display_info(self):
#        print("Title: ", self.title)
#        print("Year: ", self.year)
#        print("Publisher: ", self.publisher)
#        print("Genre: ", self.genre)
#        print("Author: ", self.author)
#        print("Price: ", self.price)

#    def input_info(self):
#        self.title = input("Enter title: ")
#        self.year = input("Enter year: ")
#        self.publisher = input("Enter publisher: ")
#        self.genre = input("Enter genre: ")
#        self.author = input("Enter author: ")
#        self.price = input("Enter price: ")


#book1 = Book("The Hobbit", 1937, "George Allen & Unwin", "Fantasy", "J.R.R. Tolkien", 10.99)
#book1.display_info()
#book1.set_price(15.99)
#print("New price: ", book1.get_price())
#book1.input_info()
#book1.display_info()

#Задание 3
#Реализуйте класс «Стадион». Необходимо хранить в
#полях класса: название стадиона, дату открытия, страну,
#город, вместимость. Реализуйте методы класса для ввода
#данных, вывода данных, реализуйте доступ к отдельным
#полям через методы класса.

class Stadium:
    def __init__(self):
        self.name = ""
        self.date = ""
        self.country = ""
        self.city = ""
        self.capacity = 0

    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def input_data(self):
        self.set_name(input("Enter stadium name: "))
        self.set_date(input("Enter opening date: "))
        self.set_country(input("Enter country: "))
        self.set_city(input("Enter city: "))
        self.set_capacity(int(input("Enter capacity: ")))

    def print_data(self):
        print("Stadium name:", self.get_name())
        print("Opening date:", self.get_date())
        print("Country:", self.get_country())
        print("City:", self.get_city())
        print("Capacity:", self.get_capacity())


stadium = Stadium()
stadium.input_data()
stadium.print_data()