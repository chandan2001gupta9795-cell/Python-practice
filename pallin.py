# Take input from user
text = input("Enter a string: ")

# Reverse the string
reversed_text = text[::-1]

# Check palindrome
if text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")