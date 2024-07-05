#  Check for Element
# Question: Check if a specific element exists in a list.
# Example Input: List: [10, 20, 30, 40], Element: 20
# Example Output: True

def check_element(values, check):
    print(check)
    for i in values:
        if i == check:
            return True
        return False
    
values = [ 10,20,30,40]
check = int(input("Enter Find Value: "))
print(check_element(values, check))