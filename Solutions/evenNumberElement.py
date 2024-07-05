# Even Numbers in a List-
# **Question**: Extract all even numbers from a list.
# - **Example Input**: `[1, 2, 3, 4, 5]`
# - **Example Output**: `[2, 4]`


values = [1, 2, 3, 4, 5]


def find_even_number(values):
    even_numbers = []
    for value in values:
        if value % 2 == 0:
            even_numbers.append(value)

    return even_numbers


print(find_even_number(values))
