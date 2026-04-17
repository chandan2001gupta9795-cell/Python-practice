# Input tuple from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# Create tuple of even numbers
even_numbers = tuple(x for x in numbers if x % 2 == 0)

# Create tuple of odd numbers
odd_numbers = tuple(x for x in numbers if x % 2 != 0)

# Output
print("Even numbers tuple:", even_numbers)
print("Odd numbers tuple:", odd_numbers)