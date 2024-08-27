# - **Question**: Sort a list of integers in ascending order.
# - **Example Input**: `[3, 1, 4, 1, 5, 9]`
# - **Example Output**: `[1, 1, 3, 4, 5, 9]`


# def sortList(values):
#     return list(values)

# value = [3,1,4,1,5,9]
# print(sortList(value))

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)  # Recursive call
        print(n)

# Example usage:
value = int(input("Enter Number: "))
try:
    number =value
    print_numbers(value)
except ValueError:
    print("Please enter a number ")