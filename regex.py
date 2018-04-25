import re

# manually checking if a string is a valid phone number
def is_phone_number(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, -1):
        if not text[i].isdecimal():
            return False

    return True

print('415-555-4242 is a phone number:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi is a phone number:')
print(is_phone_number('Moshi moshi'))

# searching for a valid phone number inside a larger string

message = 'Call me at 415-555-9999 tomorrow. 415-555-1011 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)

print('Done')

# using basic regex to search
re_phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = re_phone_number.search(message)
print(match.group())

