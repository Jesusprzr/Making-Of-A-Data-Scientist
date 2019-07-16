#QUESTION 6 - What does this produce?
vehicle = 'car'
vehicle[-1] + vehicle[1] + vehicle[:1] + 'e' + vehicle
#QUESTION 7 - Select the expression that produces True
'abc123'.isdigit()
#False
'12.34'.isalnum()
#False
'abc123'.isalnum()
#True
'apple'.upper().isupper()
#True

#QUESTION 8 - Select if produces True
s = 'VON'
s.isalpha() or s.isnumeric()
#True
s.isalpha() and s.isnumeric()
#False

#QUESTION 9 - NOT FINISHED
help(str.find)
s1 = 'banana'
s2 = 'ana'
s1.find(s2)+s1.find(s2)

#QUESTION 10 - What is printed?
digits = '0123456789'
result = 100
for digit in digits:
    result = result - int(digit)

print(result)

#QUESTION 11 - What is printed?
digits = '0123456789'
result = 0
for digit in digits:
    result = digit

print(result)

#QUESTION 12 - What is printed?
digits = '0123456789'
result = ''
for digit in digits:
    result = result + digit * 2

print(result)

#QUESTION 13 -> which option prints 'Happy 30th!'
message = 'Happy 29th!'
new_message = ''

for char in message:
    new_message = new_message + str((int(char) + 1) % 10)

print(new_message)
#Option 1 False

message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    new_message = new_message + char

print(new_message)
#option 2 False

message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    else:
        new_message = new_message + char

print(new_message)
#option 3 True

message = 'Happy 29th!'
new_message = ''

for char in message:
    if not char.isdigit():
        new_message = new_message + char
    else:
        new_message = new_message + str((int(char) + 1) % 10)
    

print(new_message)
#option 4 True

#QUESTION 14 - Create the correct function body.
def common_chars(s1, s2):
    ''' (str, str) -> str

    Return a new string containing all characters from s1 that
    appear atleast once in s2. The characters in the result 
    will appear in the same order as they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('abb','ab')
    'abb'
    '''

    res = ''
    for ch in s1:
        if ch in s2:
            res = res + ch
    return res