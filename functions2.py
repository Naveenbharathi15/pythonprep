import re


# 1.Write a program that validates a password based onthefollowingcriteria:\
#     1. Atleast 1 letter between[a - z]
#     2.Atleast 1 number between[0 - 9]
#     3.Atleast 1 letter between[A - Z]
#     4.Atleast 1 characterfrom[$  # @]
#     5.Minimum length of transaction password: 6
#     6.Maximum length of transaction password: 12

password = input()
if 6 <= len(password) <= 12:
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    for i in password:
        if 97 <= ord(i) <= 122 and flag1 == False:
            flag1 = True
        if 48 <= ord(i) <= 57 and flag2 == False:
            flag2 = True
        if 65 <= ord(i) <= 90 and flag3 == False:
            flag3 = True
        if 35 <= ord(i) <= 37 and flag4 == False:
            flag4 = True
    if flag1 == True and flag2 == True and flag3 == True and flag4 == True:
        print("Password updated successfully")
    else:
        print("Create a password which meets the above conditions")

else:
    print("Create a password which meets the above conditions")


# 2. Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# 	hello world! 123
# 	Then, the output should be:
# 	LETTERS 10
# 	DIGITS 3

line = input()
LETTERS = 0
NUMBERS = 0
for i in line:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        LETTERS = LETTERS + 1
    if 48 <= ord(i) <= 57:
        NUMBERS = NUMBERS + 1
print(LETTERS)
print(NUMBERS)


# 4. Define a function which can print a dictionary where the keys are numbers between
# 1 and 20 (both included) and the values are square of keys.
# Hints:
#     1.Use dict[key]=value pattern to put entry into a dictionary.
#     2.Use ** operator to get power of a number.
#     3.Use range() for loops.


dictionary = {}
for i in range(1, 21):
    dictionary[i] = i**2
print(dictionary)


# 5. Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.


list1 = [1, 1, 2, 3, 4, 6, 5, 9, 7]


def removedup():
    set1 = set([])
    for i in list1:
        set1.add(i)
    print(set1)


removedup()


# 6. Take two lists, and write a program that returns a list that
# contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a)
d = set(b)
h = c.intersection(d)
print(h)


# 7. Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last elements of the given list. For practice,
# write this code inside a function.


def samfun():
    a = [5, 10, 15, 20, 25]
    res = []
    res.append(a[0])
    res.append(a[-1])
    print(res)


samfun()


# 8. Take a list, write a program that prints out all the elements of the list that are less than 5


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list(i for i in a if i < 5))