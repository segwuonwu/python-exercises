# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

# def multiply_by(number, multiplier):
#     for i, num in enumerate(number):
#         number[i] = num * multiplier
#     return number

def multiply_by(dictionary, num):
    for i in dictionary:
        dictionary[i - 1] = dictionary[i - 1] * 5
    print(dictionary)


multiply_by([1, 2, 3], 5)