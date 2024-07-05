#  Reverse a List
# Question: Reverse the elements in a list.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]


def find_reverse(values):
    return values[::-1]

values = [1,2,3,4,5]

print(find_reverse(values))