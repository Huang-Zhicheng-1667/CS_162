"""
Get user's input, capitalize the first character, print the first character.
Get the first character
Capitalize the first character
Print the result
Zhicheng Huang
"""


def get_first_character(txt):
    """
    Get txt and return the frist character.
    Return text[0]
    """
    return txt[0]


def capitalize_string(txt):
    """
    Capitalize the input txt.
    capitalize(txt)
    """
    return txt.upper()


def get_user_input():
    """
    Get user's input and capitalize it.
    Get input
    Get first character
    Capitalize first character
    """
    user_input = input("Please enter a word: ")
    first_char = get_first_character(user_input)
    first_char = capitalize_string(first_char)
    return first_char


def main():
    """
    Print the result and loop back.
    If user has a invalid input, get input again.
    """
    while 1:
        first_char = get_user_input()
        print(f'The first letter you entered was: "{first_char}"')
        while 1:
            user_input = input("Do you want to exit? Y/N\n")
            if (user_input == 'Y') or (user_input == 'N'):
                break
            print("Invalid input!!!")
        if (user_input == 'Y'):
            break


if __name__ == "__main__":
    main()
