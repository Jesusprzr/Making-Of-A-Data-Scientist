#MORE STR OPERATORS
#string comparison
    #the equality and inequality operators can be applied to strings:
'a'=='a'
'bb'=='bv'
'coño_de_la_madre' == 'coño de la madre'
'az' != 'haz'
    #we can compare two strings for their dictionary order, comparing letter by letter:
'abracadabra' < 'ace'
'abracadabra' < 'abc'
'a' <= 'a'
'A' < 'B'
    #capitalization matters, capital letters have less value than lowercase letters
'A' == 'a'
'VON' < 'von'
'A' < 'b'
'a' != 'A'
    #every letter can be compared
',' < '3'
'!' == '¡'
    #we can't compare values of two different types of ordering
'a' == 3 
'100' == 100
#testing for substrings
    #the operator in checks whether a string appears anywhere inside another string.
'z' in 'sorro'
'ideo' in 'esternoclestomastoideo'
'zoo' in 'ooz'
#string lenght: fuction len
    #the build-in function len returns the number of characters in a string:
len("")
len("esternoclestomastoideo")
len("bwa"+"ha"*23)
#STR INDEXING AND SLICING
#indexing
    #an index is a position within a string. left--(0,1,2...)-->right left<--(...-3,-2,-1)right
s = 'hello world' 
s[0]
s[4]
s[5]
s[-10]
    #we can extract more than one character using slicing. Includes start of scilicing but not ending.
s[0:5]
s[6:]
s[1:-4]
s[:-1]
#modifiying strings
    #we cannot change a string
s[4] = 'y'
    #if we want to modify strings, is as the following: let's sat 'hello fcking world'
s[:5] + ' fcking' + s[5:]
    #the original strings in variable s were not modified, just added a new string "fcking" and s 
    #refered to that string, but it wasn't modified, strings cannot be modified.
#STR METHODS: FUNCTIONS INSIDE OBJECTS
#methods 
    #a methonf is a function inside of an object
    #the general form of a method call is:
        #object.method(arguments)
#string methods
    #conside the following code:
keanu = 'neon'
    #to find out which methods are inside strings, use the function dir:
dir(keanu)
dir(str)
    #for many of the string methods, a new string is returned but without changing the original.
keanu.capitalize()
keanu
    #to get information about the method:
help(str.lower)
C = 'hi There!'
for char in C:
    print(char)

