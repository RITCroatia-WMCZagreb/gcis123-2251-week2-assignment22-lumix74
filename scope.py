'''
@ASSESSME.USERID: lj7829
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = "Hello, world!"
INT_GLOBAL = 10
FLOAT_GLOBAL = 2.5

def print_param(param):
    print(f"Parameter value: {param}")

def print_local():
    local_var = "local variable"
    print(f"Local variable: {local_var}")

def print_which():
    STRING_GLOBAL = "local string"
    print(f"String global inside print_which(): {STRING_GLOBAL}")

def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)

    local_var = "Main local"
    print_local()

    print_which()
    print(f"STRING_GLOBAL in main(): {STRING_GLOBAL}")

if __name__ == "__main__":
    main()