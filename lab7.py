import sys

def check_palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"


if __name__ == "__main__":
    string = sys.argv[1]
    print(check_palindrome(string))