from password_strength_checker import check_password_strength
from vars import digits, lower_case, upper_case, special_chars, most_common_passwords, common_words, leed_speak

if __name__ == "__main__":

    # Ask for password
    password = str(input("Insert your password for strength analysis: "))

    print("################################")

    # Check password strength
    check_password_strength(password, digits, lower_case, upper_case, special_chars, most_common_passwords, common_words, leed_speak)
