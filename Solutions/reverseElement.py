#  Reverse a List
# Question: Reverse the elements in a list.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]


def find_reverse(values):
    return values[::-1]

values = [1,2,3,4,5]

print(find_reverse(values))


# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list

# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)