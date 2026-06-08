# Day 1 - Functions
# Palindrome Check

def is_palindrome(text):
    return text == text[::-1]

text = input("Enter a number: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
