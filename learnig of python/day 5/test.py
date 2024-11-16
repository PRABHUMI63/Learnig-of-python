# Code Task: Ek function find_even banao jo ek list le aur usme se sirf even numbers return kare.

def find_even(numbers):
    even_numbers = []  # List to store even numbers
    for num in numbers:
        if num % 2 == 0:  # Check if number is even
            even_numbers.append(num)  # Add even number to list
    return even_numbers

# Test the function
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = find_even(numbers_list)
print("Even numbers:", result)
