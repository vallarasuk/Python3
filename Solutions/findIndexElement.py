# Check for Element
# Question: Check if a specific element exists in a list.
# Example Input: List: [10, 20, 30, 40], Element: 20
# Example Output: True


def find_index_value(values , check):
    for i in range(len(values)):
        if values[i] == check:
            return i
         
    return "Value Not Found"       
        
values = [10,20,30,40]

check = int(input("Enter find Index Value : "))

print(find_index_value(values, check))