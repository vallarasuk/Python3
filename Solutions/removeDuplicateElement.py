#  Remove Duplicates
#  - **Question**: Remove duplicates from a list.
# - **Example Input**: `[1, 2, 2, 3, 4, 4, 5]`
# - **Example Output**: `[1, 2, 3, 4, 5]`


def remove_duplicate_values(values):
    unique_values = set(values)
    return list(unique_values)

values = [1,2,2,3,4,4,5]
print(remove_duplicate_values(values))