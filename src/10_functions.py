# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    if num % 2 == 0:
        return True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def even_num(n):
    if n % 2 == 0:
        print('Even!')
    else:
        print('Odd')

even_num(num)

