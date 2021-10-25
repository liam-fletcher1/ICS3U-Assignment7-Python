#!/usr/bin/env python3

# Created by : Liam Fletcher
# Created on : October 2021
# This program asks the user for a string
# The program with check if the string is a Palindrome
# Some information found from: https://stackoverflow.com/questions/33335318/writing-a-function-that-checks-if-a-string-is-a-palindrome

import string


def palindrome_check(palindrome, check):
    # program checks if the string is a pallindrom

    reverse = []
    palindrome = palindrome.replace(" ", "")
    palindrome = palindrome.lower()
    palindrome = palindrome.replace(".", "")

    for loop_count in range(check):
        user_input = check - loop_count
        user_input_two = user_input - 1
        reverse.append(palindrome[user_input_two:user_input])

    reverse = "".join(reverse)

    if reverse == palindrome:
        yes = True
        return yes
    else:
        no = False
        return no


def main():
    # Get user input and tells user answer

    # input
    palindrome = input("Enter a string to check for Palindrome: ")
    print("")
    check = len(palindrome)
    answer = palindrome_check(palindrome, check)

    # output
    if answer is True:
        print("{0} is a Palindrome.".format(palindrome))
    if answer is False:
        print("{0} is not a Palindrome".format(palindrome))

    print("\nDone.")


if __name__ == "__main__":
    main()
