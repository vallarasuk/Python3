# Average of Elements
# Question: Compute the average of the elements in a list.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: 3.0


def find_average_value(values):
    return sum(values) / len(values)

values = [1,2,3,4,5]

print(find_average_value(values))

