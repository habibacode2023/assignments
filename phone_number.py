import re

def Az_phone_number(number):
    # Remove any spaces, dashes or other special characters from the number
    number = re.sub(r'\s+|-', '', number)

    #Checks if the given phone number belongs to Azerbaijan or not.
    #Returns True if it's an Azerbaijan mobile number, False otherwise.
    
    pattern = r"^(?:\+994|0)(5[0157]|7[07]|99)[\d]{7}$"
    match = re.match(pattern, number)
    return bool(match)

# Test:
print(Az_phone_number("+994501234567")) # True
print(Az_phone_number("0551234567"))   # True
print(Az_phone_number("+99455123456")) # False
print(Az_phone_number("0123456789"))   # False
print(Az_phone_number("050-345-67-89")) # True
print(Az_phone_number("077 345 66 89")) # True
print(Az_phone_number("876 345 66 89")) # False
