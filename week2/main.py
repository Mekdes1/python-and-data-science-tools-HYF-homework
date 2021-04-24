"""
Write a function called fizz_buzz that takes a number
a. If the number is divisible by 3, it should return “Fizz”.
b. If it is divisible by 5, it should return “Buzz”.
c. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
d. Otherwise, it should return the same number.
"""


def fizz_buzz():
    number = int(input('Please in put number:'))
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number


# print(fizz_buzz())

# Consider a lst= [5, 10, 20] and write a try and except block to avoid IndexError.


def number_picker():
    sample_list = [5, 10, 20]
    try:
        choose_index = int(input('Please choose index of the number you want to print: '))
        print(f'your number is {sample_list[choose_index]}')
    except IndexError:
        print("Exception Error: Please make sure the index you entered is in range")


# number_picker()

# Create a class of Jet inventory with two arguments i.e name and country. Also add the minimum 2 items in the class and print them.

class JetInventory:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def my_first_inventory(self):
        print(f'1. {self.name} {self.country}')

    def my_second_inventory(self):
        print(f'2. {self.name} {self.country}')


my_first_inventory_is = JetInventory("Mekdes", "Denmark")
my_first_inventory_is.my_first_inventory()

my_second_inventory_is = JetInventory("Mekdes", "Addis")
my_second_inventory_is.my_second_inventory()

# Write a Python script to check whether a given key already exists in a dictionary.
sample_dictionary = {'name': 'Mek', 'Country': 'Ethiopia', 'City': 'Addis', 'age': 25}


def is_key_present(key):
    if key in sample_dictionary:
        print(f'{key} : {sample_dictionary[key]}')
    else:
        print(f'{key} is not present in the dictionary')


is_key_present('name')
is_key_present('height')

"""
Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 
and limit with a label to identify the even and odd numbers.
For example, if the limit is 3, it should print:
• 0 EVEN
• 1 ODD
• 2 EVEN
• 3 ODD
"""


def show_numbers(limit):
    number_in_range = range(limit + 1)
    for num in number_in_range:
        if num % 2 == 0:
            print(f'{num} EVEN')
        else:
            print(f'{num} ODD')


show_numbers(5)


# Create a class named Person, with firstname and lastname properties, and a print name method.


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        print(f'Hello {self.first_name} {self.last_name}')


show_name = Person('Mekdes', 'Habtamu')
show_name.name()


# Write a program asks for numeric user input. Instead the user types characters in the input box. The program normally would crash.
# But write try-except block so it can be handled properly.

def display_number():
    try:
        number = int(input('Enter number:'))
        print(f'Number:{number}')
    except ValueError:
        print('Please make sure you entered an integer')


# display_number()

# Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are
# instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.

class Student:
    pass


class Marks:
    pass


students = Student()
mark = Marks()
print(f'Is students an instance of Student? {isinstance(students, Student)}')
print(f'Is mark an instance of Student? {isinstance(mark, Student)}')
print(f'Is mark an instance of Marks? {isinstance(mark, Marks)}')

print(f'Is Student the subclass of the built-in object class? {issubclass(Student, object)}')
print(f'IS Marks the subclass of the built-in object class? {issubclass(Marks, object)}')
