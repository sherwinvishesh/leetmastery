# Exercise 1: Calculate the multiplication and sum of two numbers
## Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def exercise_1(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
    

# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

def exercise_2(num):
    current = 0
    for i in range(0,num,1):
        print(f'Current Number: {i} Previous Number: {current} Sum: {i + current}')


# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.

def exercise_3(string):
    for i in range(0,len(string),2):
        print(f'index[{i}] = {string[i]}')

# Exerise 4:  Remove first n characters from a string

def exercise_4(string, n):
    return string[n:]

# Exercise 5: Check if the first and last numbers of a list are the same

def exercise_5(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False
    
# Exercise 6: Display numbers divisible by 5

def exercise_6(lst):
    for i in lst:
        if i % 5 == 0:
            print(i)

# Exercise 7: Find the number of occurrences of a substring in a string

def exercise_7(string, substring):
    return string.count(substring)

# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

def exercise_8(num):
    for i in range (1,num+1,1):
        for j in range (i):
            print(i, end = ' ')
        print('\n')      

# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.

def exercise_9(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")
    


# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.


def exercise_10(lst1, lst2):
    new_lst == []
    for i in lst1:
        if i % 2 != 0:
            new_lst.append(i)
    for i in lst2:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst

# Exercise 11: Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def exercise_11(number):
    while number > 0:
        reminder = number % 10
        print(reminder, end = ' ')
        number = number // 10

#Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

def exercise_12(income):
    print("Given income", income)

    if income <= 10000:
        tax_payable = 0
    elif income <= 20000:
        # no tax on first 10,000
        x = income - 10000
        # 10% tax
        tax_payable = x * 10 / 100
    else:
        # first 10,000
        tax_payable = 0

        # next 10,000 10% tax
        tax_payable = 10000 * 10 / 100

        # remaining 20%tax
        tax_payable += (income - 20000) * 20 / 100

    print("Total tax to pay is", tax_payable)
    return True 

# Exercise 13: Print multiplication table from 1 to n
# 1  2 3 4 5 6 7 8 9 10 		
# 2  4 6 8 10 12 14 16 18 20 		
# 3  6 9 12 15 18 21 24 27 30 		
# 4  8 12 16 20 24 28 32 36 40 		
# 5  10 15 20 25 30 35 40 45 50 		
# 6  12 18 24 30 36 42 48 54 60 		
# 7  14 21 28 35 42 49 56 63 70 		
# 8  16 24 32 40 48 56 64 72 80 		
# 9  18 27 36 45 54 63 72 81 90 		
# 10 20 30 40 50 60 70 80 90 100

def exercise_13(n):
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            print(i*j, end = ' ')
        print('\n')


# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


# Exercise 15: Get an int value of base raises to the power of exponent
def exercise_15(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)
    return True



