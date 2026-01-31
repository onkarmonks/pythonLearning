# This is a sample Python script.
import keyword

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def calculations():
    # Use a breakpoint in the code line below to debug your script.
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")

    print(f'Addition - {first} + {second} = {int(first) + int(second)}')
    print(f'Subtraction -  {first} - {second} = {int(first) - int(second)}')
    print(f'Multiplication - {first} * {second} = {int(first) * int(second)}')
    print(f'Division - {first} / {second} = {int(first) / int(second)}')

def greetings():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    print(f"Hello, {first} {last}! Welcome to the Python program")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculations()
    greetings()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
