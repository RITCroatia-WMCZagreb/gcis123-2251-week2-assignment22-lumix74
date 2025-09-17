'''
@ASSESSME.USERID: lj7829
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

def add_chars(char1, char2):
    sum_value = ord(char1) + ord(char2)
    print(f"Sum of ASCII values: {sum_value}")
    if 0 <= sum_value <= 127:
        print(f"Characters for sum: {chr(sum_value)}")
    else:
        print("Sum is out of valid ASCII range")

def subtract_chars(char1, char2):
    diff_value = ord(char1) - ord(char2)
    print(f"Sum of ASCII values: {diff_value}")
    if 0 <= diff_value <= 127:
        print(f"Characters for difference: {chr(diff_value)}")
    else:
        print("Difference is out of valid ASCII range")

def main():
    char1 = input("Enter the first character: ")
    char2 = input("Enter the second character: ")

    if len(char1) != 1 or len(char2) != 1:
        print("Error")
        return
    
    add_chars(char1, char2)
    subtract_chars(char1, char2)

if __name__ == "__main__":
    main()

    #Comment#1: Sometimes odd characters or nothing appear because the result of adding or subtracting ASCII values can be outside the printable ASCII range (0-127)
    #When that happens, the characters can't be displayed.

    #Comment#2: It gives error because it works with only single character.
    #That's why the program checks the input length and shows an error message if it's not valid.

