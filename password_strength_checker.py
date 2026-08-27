""" 
Check:
- Size: 
    - length
- Possible characters 
    - number of digits
    - number of lower case letters
    - number of upper case letters
    - number of special characters
- Knows passwords:
    - presence of known passwords
- Password dependent
    - presence of repeated characters
    - presence of sequential characters
    - presence of sequential characters in keyboard
    - change of letters by numbers in known words


Rank based on:
- Each check is given a value from 1-10
- Calculate the medium or other statistic value


Steps:
1. Input password
2. Validate password
3. Analyze password / give score
4. Print out password strength

"""

from typing import List

# Possible characters in a password:
digits = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "!@#$%&*()-_=+[]{}\\/?:;<>,.~^'\" "


# Patterns in passwords: 
most_common_passwords = [
    "123456",
    "admin",
    "12345678",
    "123456789",
    "12345",
    "password",
    "Aa123456",
    "1234567890",
    "Pass@123",
    "admin123",
    "1234567",
    "123123",
    "111111",
    "12345678910",
    "P@ssw0rd",
    "Password",
    "Aa@123456",
    "admintelecom",
    "Admin@123",
    "112233",
]

common_words = [
    "admin",
    "password",
]

leed_speak = {
    "a": ["4", "@"], 
    "b": ["8"], 
    "c": ["(", "[", "<"], 
    "e": ["3"], 
    "g": ["6"], 
    "h": ["#"], 
    "i": ["1", "!", "|"], 
    "o": ["0"], 
    "s": ["5", "$"], 
    "t": ["7"],
}


# Ask for password
password = str(input("Insert your password for strength analysis: "))


# Check password length
def check_password_length(password: str) -> int:
    if (len(password) < 12):
        print("Your password is too short. Should be at least 12 characters longs.")
    return len(password)



# Analyze chars count
def analyse_chars_count(password: str, digits: str, lower_case: str, upper_case: str, special_chars: str) -> int:

    count_digits, count_lower, count_upper, count_special = count_chars(password, digits, lower_case, upper_case, special_chars)
    zeros = 0
    length = len(password)

    if (count_digits == 0):
        zeros += 1
        print("Your password should have at least 1 number.")
    if (count_lower == 0):
        zeros += 1
        print("Your password should have at least 1 lower case letter.")
    if (count_upper == 0):
        zeros += 1
        print("Your password should have at least 1 upper case letter.")
    if (count_special == 0):
        zeros += 1
        print("Your password should have at least 1 special character.")

    digits_pct = round(count_digits / length * 100, 2)
    lower_pct = round(count_lower / length * 100, 2)
    upper_pct = round(count_upper / length * 100, 2)
    special_pct = round(count_special / length * 100, 2)

    return [zeros, digits_pct, lower_pct, upper_pct, special_pct]

# Check the count of each character type:
def count_chars(password: str, digits: str, lower_case: str, upper_case: str, special_chars: str, 
                count_digits=0, count_lower_case=0, count_upper_case=0, count_special=0) -> List[int]:
    for c in password:
        if (c in digits):
            count_digits += 1
        elif (c in lower_case):
            count_lower_case += 1
        elif (c in upper_case):
            count_upper_case += 1
        elif (c in special_chars):
            count_special += 1

    return [count_digits, count_lower_case, count_upper_case, count_special]



# Check for common passwords, (password, admin, ...):
def check_presence_of_known_words(password: str, most_common_passwords: str) -> bool:
    if (password in most_common_passwords):
        print("Your password is a well known password. Choose a less generic one.")
    return  password in most_common_passwords



# Check presence of repeated characters (aa, bbb, ...)
def check_repeated_characters(password: str) -> float:
    repetitions = []

    i = 0
    j = 1
    while (i < len(password)-1):
        while (j < len(password)):

            if (password[i] == password[j]):
                if (j == len(password)-1):
                    break
                else:
                    j += 1
            else:
                break

        if (j == len(password)-1):
            # end of word is repetition
            if (password[i] == password[j]):
                repetitions.append(password[i:j+1])
                break
            # end of word is not repetition
            else:
                break
        # repeteition at the middle of the word
        elif (password[i] != password[j]) and (i < j-1):
            repetitions.append(password[i:j])
            if (j == len(password)-1):
                break

        i = j
        j = i+1

    total_repetitions = 0

    if (len(repetitions) != 0):
        print("Your password should not repeat characters:", repetitions)
        for rep in repetitions:
            total_repetitions += len(rep)
    
    return round(total_repetitions/len(password) * 100, 2)



# Check presence of sequential characters (123, abc, AbC, ...)
def check_sequences(password: str, digits: str, lower_case: str, special_chars: str) -> float:

    sequences = []
    lower_password = password.lower()
    is_sequence = False

    i = 0
    j = 1
    while (i < len(password)-1):

        if (lower_password[i] in special_chars):
            i += j
            j = i+1
        else:
            index_i = get_index(lower_password, digits, lower_case, i)

            while (j < len(password)):

                if (lower_password[j] in special_chars):
                    is_sequence = False
                    break
                
                index_j = get_index(lower_password, digits, lower_case, j)

                if (i == j-1): # fix pointer i
                    if ((index_i == index_j-1) and (same_types(lower_password, i, j))):
                        if (j == len(password)-1):
                            is_sequence = True
                            break
                        else:
                            j += 1
                    else:
                        break

                else: # once pointer is fixed, compare j-1 and j
                    if ((get_index(lower_password, lower_case, digits, j-1) == index_j-1) and (same_types(lower_password, j-1, j))):
                        if (j == len(password)-1):
                            is_sequence = True
                            break
                        else:
                            j += 1
                    else:
                        is_sequence = False
                        break
            
            if (j == len(password)-1 and is_sequence):
                if (is_sequence): # last char is sequence
                    sequences.append(password[i:j+1])
                    break
                else: # last char is not sequence
                    sequences.append(password[i:j])
                    break

            # "not is_sequence" from j-1 and j perspective, not i and j-1
            elif (not is_sequence) and (i < j-1):
                sequences.append(password[i:j])
                if (j == len(password)-1):
                    break

            i = j+1 if (lower_password[j] in special_chars) else j
            j = i+1


    total_sequences = 0

    if (len(sequences) != 0):
            print("Your password should not have characters in sequence:", sequences)
            for seq in sequences:
                total_sequences += len(seq)
        
    return round(total_sequences/len(password) * 100, 2)

def get_index(password: str, digits: str, lower_case: str, index: str) -> int:
    return digits.index(password.lower()[index]) if password.lower()[index] in digits else lower_case.index(password.lower()[index])

def same_types(password: str, i: str, j: str) -> bool:

    password_lower = password.lower()
    i_str = password_lower[i]
    j_str = password_lower[j]
    
    if (is_int(i_str) and is_int(j_str)) or ((not is_int(i_str)) and (not is_int(j_str))):
        return True
    else: 
        return False

def is_int(str: str) -> bool:
    try:
        return type(int(str)) == int
    except ValueError:
        return False



# Check leet code in known words (p45$w0rd, @dm1n, ...)
def check_leet_code(password: str, lower_case: str, common_words: str, leed_speak: str) -> bool:

    words_replaced = []

    password_lower = password.lower()

    changed_password_list = list(password_lower)

    # Populate dict with password index and its leet code replacement
    for i in range(len(password_lower)):
        char = password_lower[i] 
        if (char not in lower_case):
            for key, value in leed_speak.items():
                if (char in value):
                    changed_password_list[i] = key

    changed_password = "".join(changed_password_list)

    # Check all substrings from changed_password in common_words
    substrings = set([changed_password[i:j] for i in range(len(changed_password)) for j in range(i+1, len(changed_password)+1)])

    # Here, this takes longer than the reverse logic, but in a real case scenario, len(common_words) > len(substrings)
    for sub in substrings:
        if sub in common_words:
            words_replaced.append(sub)
            print("Your password should not be a word with replaced letters:", sub)

    return (len(words_replaced) != 0)





# Check password strength
def check_password_strength(password, digits, lower_case, upper_case, special_chars, most_common_passwords, common_words, leed_speak):

    # Check password length
    length = check_password_length(password)        

    # Check count of each character type
    zeros, digits_pct, lower_pct, upper_pct, special_pct = analyse_chars_count(password, digits, lower_case, upper_case, special_chars)

    # Check for common passwords
    has_known_passwords = check_presence_of_known_words(password, most_common_passwords)

    # Check repeated characters
    repeated_pct = check_repeated_characters(password)

    # Check presence of sequential characters
    sequences_pct = check_sequences(password, digits, lower_case, special_chars)

    # Change of letters by numbers in known words
    has_leet_code_words = check_leet_code(password, lower_case, common_words, leed_speak)


    print("################################")
    password_strength = "Password strength: "
    if ((length < 12) or has_known_passwords or has_leet_code_words or zeros > 0):
        password_strength += "Weak"
    else:
        if (repeated_pct + sequences_pct >= 20.00):
            password_strength += "Medium"
        else:
            if (repeated_pct + sequences_pct > 0) or ((digits_pct or lower_pct or upper_pct or special_pct) >= 75.00):
                password_strength += "Strong"
            else:
                password_strength +="Very strong"
    print(password_strength, "\n################################")

    return

check_password_strength(password, digits, lower_case, upper_case, special_chars, most_common_passwords, common_words, leed_speak)
