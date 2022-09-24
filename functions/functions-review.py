# Assignment 1
# this takes the last letter of the word to the 70th column
def right_justify(s):
    length = len(s)
    spaces = 70 - length
    print((" " * spaces) + s)


word = "monty"
right_justify(word)


# Takes the last letter of the word to the 50th column
def test_work(s):
    length = len(s)
    spaces = 50 - length
    print((" " * spaces) + s)


word = "MONTY"
test_work(word)


# Assignment 2a
# The function takes two parameters and arguments and calls each to be printed twice
def do_twice(name, school):
    print(name, school)


def print_spam():
    print("spam")


print("Name of Students and their schools")
do_twice("James Stratoff", "Sam International School")
print("Done")


# Assignment 2b
# Takes four parameters and calls the function twice
# Copy the definition of print_twice from earlier in this chapter to your script.
# Use the modified version of do_twice to call print_twice twice, passing 'spam' as
# an argument.
def do_twice(name, school):
    print(name, school)
    print(name, school)


def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice(" ", print_twice("spam"))


# Assignment3
# Define a new function called do_four that takes a function object and a value and
# calls the function four times, passing the value as a parameter. There should be only
# two statements in the body of this function, not four.

def do_four(first_name, last_name):
    print(first_name, last_name)
    print(first_name, last_name)


do_four("Vida", "Ahyia")
do_four("Vida", "Ahyia")
