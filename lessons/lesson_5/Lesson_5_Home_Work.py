# Beginner Python Homework: Introduction to Basics

def print_hello_world():
    """Task 1: Print 'Hello, World!' to the console."""
    print("Hello World")

def create_and_print_variables():
    """Task 2: Create two variables, `greeting` with any text and `number` with any number, then print both."""
    print("\n=== Greetings and Numbers ===")
    a_greeting = "Hello!"
    a_number = 12
    print("Greeting:", a_greeting)
    print("Number:", a_number)

    greeting = 'Good morning'
    number = 42
    print(greeting, number)


def sum_two_numbers():
    """Task 3: Create two variables with numbers and print their sum."""
    number_a = 4
    number_b = 3
    print(number_a + number_b)

    a = 10
    b = 5
    print("the sum is:", a + b)


def greet_user():
    """Task 4: Use the input() function to ask the user for their name and greet them."""
    print("What is your name?")
    name = input()
    print("Hello,", name)

    name = input('What is your name?')
    print ('Hello', name)

def create_list():
    """Task 5: Create a list named `fruits` with any three fruits and print the list."""
    print("\n=== Fruits ===")
    a = ("\n apple")
    b = ("\n banana")
    c = ("\n orange")
    print("List of fruits:", a, b, c)

    fruits = ['apple', 'banana', 'cherry']
    print(fruits)

def add_fruit_to_list(fruits):
    """Task 6: Add another fruit to the `fruits` list and print the updated list."""
    print("\n=== Fruits ===")
    a = 'apple'
    b = 'banana'
    c = 'orange'
    a_list = [a, b, c]
    print("List of fruits:", a, b, c)
    a_list.append("peach")
    print("New list:", a_list)

    fruits = ['apple', 'banana', 'cherry']
    print(fruits)
    fruits.append('orange')
    print(fruits)

def print_fruits(fruits):
    """Task 7: Print each fruit in the `fruits` list using a loop."""
    a = ("apple")
    b = ("banana")
    c = ("orange")
    print("Fruit Loop:")
    for i in [a, b, c]:
        print(i)

    fruits = ['apple', 'banana', 'cherry']
    for fruit in fruits:
        print(fruit)

def create_and_print_dictionary():
    """Task 8: Create a dictionary named `person` with keys 'name' and 'age', then print the dictionary."""
    Dict = {1: 'Name', 2: 'Age'}
    print("Person Dictionary: ", Dict)

    person = {"name": "John", "age": 38}
    print(person)

def update_age_in_dictionary(person):
    """Task 9: Update the 'age' in the `person` dictionary to a new value and print the updated dictionary."""
    person = {"name": "John", "age": 38}
    print(person)
    person['age'] = 44
    print(person)

def check_number_greater_than_10():
    """Task 10: Check if a number stored in a variable is greater than 10 and print a relevant message."""
    n = 12
    if n > 5:
        print("Number is greater than 10")
    else:
        print("Number is 10 or less")

    number = 12
    if number > 10:
        print(number, 'is greater than 10')
    else:
        print(number, 'is less than 10')


def main():
    # Call each function to execute the tasks
    print_hello_world()
    create_and_print_variables()
    sum_two_numbers()
    greet_user()
    fruits = create_list()
    add_fruit_to_list(fruits)
    print_fruits(fruits)
    person = create_and_print_dictionary()
    update_age_in_dictionary(person)
    check_number_greater_than_10()

if __name__ == "__main__":
    main()
