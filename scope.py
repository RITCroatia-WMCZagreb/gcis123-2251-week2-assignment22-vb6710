'''
@ASSESSME.USERID: vb6710
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL = "Hellooooo guyssssss!!!!"
INT_GLOBAL = 12345
FLOAT_GLOBAL = 3.14159


def print_param(para):
    print("Parameter value :", para, sep=" ")

def print_local():
    local = "local variable"
    print("Local variable:", local, sep=" ")

def print_which():
    print("Global string: ", STRING_GLOBAL, sep=" ")

def main():
    print_param(STRING_GLOBAL)
    print_param(INT_GLOBAL)
    print_param(FLOAT_GLOBAL)

    print_local()
    print_which()
    print("Global variable:", STRING_GLOBAL)

if __name__ == "__main__":
    main()