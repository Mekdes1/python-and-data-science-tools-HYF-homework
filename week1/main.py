# Homework exercises for Week #1
# python script to print your name and age
import random
name = 'Mekdes Habtamu'
age = 25
print(f'Name: {name} Age: {age}')

# Create a list of your 5 favorite movies and store it in the variable
my_favorite_movies=['Ratatouille','Manchester by the Sea','The Godfather','Rear Window','Boyhood',]
print(f'My favorite movies are: {my_favorite_movies}')

#Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
first_and_last_colors = (f'{color_list[0]} and { color_list[-1]}')
print('The first and last colors from the color_list are:', first_and_last_colors)

#Write a Python script to add a key to a dictionary
sample_dictionary = {0: 10, 1: 20}
sample_dictionary[2] = 30
print(sample_dictionary)

#Write a Python program to calculate body mass index.
def body_mass_index_calculator():
    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    weight = float(input('Enter your weight (kg): '))
    height = float(input(f'Enter your height ({"m2".translate(superscript)}): '))
    body_mass_index = weight / height ** 2
    return  (f'your body mass index is: {round(body_mass_index, 2)}')
print(body_mass_index_calculator())

#Additional Exercises:
#Guess a number game - between 1 to 9.
def guess_number_game():
    random_number = random.randint(1, 9)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input('Enter your number guess between 1 to 9 : '))
    print('Well guessed !')

guess_number_game()

#Create a tuple with different data types
sample_tuple = ('tuple', 50, 1.4, True)
print(sample_tuple)

#Create a list of 5 city names and convert it into tuples.
def convert_to_tuples(list):
    return tuple(list)
sample_list = ['Dubai','Paris',8,9,10]
print(convert_to_tuples(sample_list))

#Remove duplicated from the list and store the values in the same list:

def convert_to_non_duplicated_list(duplicated_list):
    non_duplicated_set = set(duplicated_list)
    return list(non_duplicated_set)

sample_duplicated_list = [10,20,30,20,10,50,60,40,80,50,40]

print(convert_to_non_duplicated_list(sample_duplicated_list))

#Accept a string from user and remove the characters which have odd index values of a given string and print them

def odd_index_remover():
    given_string= str(input('Please enter your string: '))
    string_with_removed_index= ''

    for i in range(len(given_string)):
        if(i % 2 == 0):
           string_with_removed_index= (f'{string_with_removed_index}{given_string[i]}')

    print(f'Given string:- {given_string}')
    print(f'Sting with removed indes:- {string_with_removed_index}')


odd_index_remover()