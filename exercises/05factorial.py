# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#

def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
    
# def fact(num):
#     # start at number 1 instead of 0
#     result = 1
#     # iterate and count up through each number until we get to 1
#     for x in range(result, (num + 1)):
#         result = result * x
#     return result

# print(fact(5))