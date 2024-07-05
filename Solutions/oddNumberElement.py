# Odd Numbers in a List
# Question: Extract all odd numbers from a list.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [1, 3, 5]

values = [1, 2, 3, 4, 5]


def find_odd_number(values):
    odd_numbers = []
    for value in values:
        if value % 2 != 0:
            odd_numbers.append(value)
        
    return odd_numbers
        

print(find_odd_number(values))
