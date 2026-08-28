# Password strength checker
An script that takes as an input a password from the user, analyzes it and return the strength of such based on criteria

## Table of contents
- [Built with](#built-with)
- [Project Structure](#project-structure)
- [Criteria](#criteria)
- [How to use it](#how-to-use)

<a name="built-with">

## Built with
This project was entirely built with python 3.13.5.


<a name="project-structure">

## Project Structure
```
Root()
 ├─ main.py                   → Main function
 ├─ password_strength_checker → Actual algorithm
 └─ vars.py                   → Variables such as "digits" and "most_common_words"
```

<a name="criteria">

## Criteria

### Characters, words and codes considered
#### The following characters when analysing a password:
- digits = "0123456789"
- lower_case = "abcdefghijklmnopqrstuvwxyz"
- upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
- special_chars = "!@#$%&*()-_=+[]{}\\/?:;<>,.~^'\" "

#### The following words were considered when analyzed a password:
- most_common_passwords = [
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

- common_words = [
    "admin",
    "password",
]

#### The following leet code was considered when analyzing a password:
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
    "t": ["7"]
}




### The project uses the following criteria to evalute the strength of a password
1. Length
2. Presence of digits (1, 2, 3...)
3. Presence of lower case letters (a, b, c...)
3. Presence of upper case letters (A, B, C...)
4. Presence of special characters (!, @, #...)
5. Use of a well-known password (password, admin, 12345678...)
6. Presence of repeated following characters (aaa, bbb, 111)
7. Presence of sequence characters (abc, 123, AbC...)
8. Presence of leet code that when decyphered turns into a well-known passowrd (p46$w0rd --> password)


### Reasoning
- Items 2.1.1, 2.1.2 and 2.1.3 of [OWASP TOP 10 Password Security Requirements] (https://owasp-aasvs4.readthedocs.io/en/latest/V2.1.html) were considered when developing criterias 1, 4 and 5
-[Nist ] (https://pages.nist.gov/800-63-3/sp800-63b.html) were considered for criteria 7 
- Other criterias were considered from previous life experience and personal reasoning


### Strength evaluation
The following logic is used when analyzing a password:
- Not meeting the minimum requirements: Weak
- Minimum requirements + few repetitions and sequences: Medium
- Minimum requriments + no repetetions + no sequences: Strong
- Minimum requiremetns + no repetitions + no sequences + no predominant character type: Very strong
```
if ((length < 12) or in_known_passwords or has_leet_code_words or zeros > 0):
        password_strength += "Weak"
else:
    if (repeated_pct + sequences_pct + reversed_sequences_pct >= 20.00):
        password_strength += "Medium"
    else:
        if (repeated_pct + sequences_pct + reversed_sequences_pct > 0) or ((digits_pct or lower_pct or upper_pct or special_pct) >= 75.00):
            password_strength += "Strong"
        else:
            password_strength +="Very strong"
```



<a name="how-to-use">

## How to use it
Simply run this on a terminal under the project directory if you have python installed
```
> python3 main.py
```
