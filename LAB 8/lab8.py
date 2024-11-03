"""
Author: Ved Vyas
Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
Functionality of code: This is my Lab 8 project where I implemented several recursive functions 
to solve different problems. I wrote code for finding list length recursively, performing integer 
division without using the division operator, summing digits of a number, displaying numbers in 
reverse, and implementing binary search. Each exercise helped me understand different aspects 
of recursive problem-solving.
"""

#EXERCISE 1 
def mylen(some_list):
    # In this function, I'm implementing a recursive way to find the length of a list
    # First, I check for my base case - an empty list
    if not some_list:
        # If the list is empty, I return 0 as its length
        return 0
    # For my recursive case, I'm breaking down the problem:
    # I count 1 for the current element, then recursively find length of rest of list
    else:
        return 1 + mylen(some_list[1:])

def main():
    # Here I'm testing my mylen function with a sample list
    alist = [43, 76, 97, 86]
    # I print the result to verify my recursive length calculation works
    print(mylen(alist))

if __name__ == "__main__":
    main()


#EXERCISE 2
def intDivision(dividend, divisor):
    # I'm implementing integer division recursively without using the division operator
    # First, I validate my inputs to make sure they're valid integers and divisor isn't zero
    if not isinstance(dividend, int) or not isinstance(divisor, int) or divisor == 0:
        raise ValueError("Invalid inputs. Both dividend and divisor should be integers, and divisor should not be 0.")

    # I need to handle negative numbers properly, so I determine the sign of my result
    # Using XOR operator to check if only one number is negative
    sign = 1
    if (dividend < 0) ^ (divisor < 0):
        sign = -1 

    # I'll work with absolute values to make the recursion simpler
    dividend = abs(dividend)
    divisor = abs(divisor)

    # My base case: when dividend becomes smaller than divisor
    if dividend < divisor:
        return 0
    # In my recursive case, I subtract divisor from dividend and count how many times I can do this
    else:
        result = 1 + intDivision(dividend - divisor, divisor)
        # Finally, I apply the sign I determined earlier
        return result * sign

def main():
    try:
        # Getting user input for my division operation
        n = int(input('Enter an integer dividend: '))
        m = int(input('Enter an integer divisor: '))

        # Performing the division and showing the result
        print('Integer division', n, '//', m, '=', intDivision(n, m))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


#EXERCISE 3
def sumDigits(some_num):
    # I'm writing a function to sum all digits in a number recursively
    # First, making sure my input is valid
    if not isinstance(some_num, int) or some_num <= 0:
        raise ValueError("Invalid input. Please provide a positive integer.")

    # My base case: when I have a single digit
    if some_num < 10:
        return some_num
    # For my recursive case, I add the last digit and recursively sum the rest
    else:
        return some_num % 10 + sumDigits(some_num // 10)

def main():
    try:
        # Getting the number from user to sum its digits
        number = int(input('Enter a number: '))

        # Calculating and showing the sum of digits
        print(sumDigits(number))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


#EXERCISE 4
def reverseDisplay(some_num):
    # Here I'm writing a function to display a number in reverse order
    # First checking if my input is valid
    if not isinstance(some_num, int) or some_num <= 0:
        raise ValueError("Invalid input. Please provide a positive integer.")

    # My base case: when I have a single digit number
    if some_num < 10:
        print(some_num, end="")
    # For my recursive case, I print the last digit first, then handle the rest
    else:
        print(some_num % 10, end="")
        reverseDisplay(some_num // 10)

def main():
    try:
        # Getting the number to reverse from the user
        number = int(input('Enter a number: '))

        # Displaying the number in reverse
        reverseDisplay(number)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


#EXERCISE 5
def binary_search2(key, alist, low, high):
    # I'm implementing a recursive binary search algorithm
    # My base case: when the search space is exhausted
    if low > high:
        return 'Item is not in the list'

    # Finding the middle point for my binary search
    guess = (high + low) // 2

    # Checking if I found my key
    if key == alist[guess]:
        return guess
    # If my key is smaller, I search in the left half
    elif key < alist[guess]:
        return binary_search2(key, alist, low, guess - 1)
    # If my key is larger, I search in the right half
    else:
        return binary_search2(key, alist, guess + 1, high)

def main():
    # Creating my sorted test list
    some_list = [-8, -2, 1, 3, 5, 7, 9]

    # Testing my binary search with different scenarios:
    # Testing search for last element
    print(binary_search2(9, some_list, 0, len(some_list) - 1))
    # Testing search for first element
    print(binary_search2(-8, some_list, 0, len(some_list) - 1))
    # Testing search for non-existent element
    print(binary_search2(4, some_list, 0, len(some_list) - 1))

if __name__ == "__main__":
    main()