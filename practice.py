def print_letter(letter):
    """
    Prints a single letter in ASCII art.
    """
    rows = 7  # Height of the letters
    if letter == 'A':
        for i in range(rows):
            for j in range(rows):
                if (i == 0 and j != 0 and j != rows - 1) or \
                   (i > 0 and (j == 0 or j == rows - 1)) or \
                   (i == rows // 2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'B':
        for i in range(rows):
            for j in range(rows):
                if j == 0 or \
                   (j == rows - 1 and (i != 0 and i != rows - 1 and i != rows // 2)) or \
                   (i == 0 or i == rows - 1 or i == rows // 2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'C':
        for i in range(rows):
            for j in range(rows):
                if (j == 0) or \
                   (i == 0 and j != rows - 1) or \
                   (i == rows - 1 and j != rows - 1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'D':
        for i in range(rows):
            for j in range(rows):
                if j == 0 or \
                   (j == rows - 1 and (i != 0 and i != rows - 1)) or \
                   (i == 0 or i == rows - 1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    # Add similar conditions for E to Z
    # Here is an example for 'E' and 'F'
    elif letter == 'E':
        for i in range(rows):
            for j in range(rows):
                if j == 0 or \
                   (i == 0) or \
                   (i == rows // 2) or \
                   (i == rows - 1):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    elif letter == 'F':
        for i in range(rows):
            for j in range(rows):
                if j == 0 or \
                   (i == 0) or \
                   (i == rows // 2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        print("Letter not supported")

def print_alphabet():
    """
    Prints the alphabet from A to Z.
    """
    for letter in range(ord('A'), ord('Z') + 1):
        print_letter(chr(letter))
        print()  # Newline after each letter

# Call the function to print A to Z
print_alphabet()
