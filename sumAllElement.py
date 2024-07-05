#  Sum of All Elements
# Question: Given a list of integers, find the sum of all elements.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: 15


value = [1, 2, 3, 4, 5]

sums = 0

if len(value) > 1:
    for i in value:
        sums = sums + i
print(sums)


# alternative method using in-build function

def total_sum(values):
    return sum(values)

val = [1,2,3,4,5,6,7,8,9,10]

print(total_sum(val))