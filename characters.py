'''
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

def add_chars(char1, char2):
    character1 = ord(char1)
    character2 = ord(char2)
    sum = character1 + character2
    sum_char = chr(sum)
    print("Sum of a and b =" , sum,sep=" ",end="\n")
    print("Character =", sum_char ,sep=" ")   
 
 
 
def substract_chars(char3,char4):
    character3 = ord(char3)
    character4 = ord(char4)
    substract = character3 - character4 
    characters=chr(substract)
    print("Difference of c and d =", substract, sep=" ", end="\n")
    print("character=", characters, sep=" ")

def main():
    add_chars("a","b")
    substract_chars("c","a")

if __name__ == "__main__":
    main()