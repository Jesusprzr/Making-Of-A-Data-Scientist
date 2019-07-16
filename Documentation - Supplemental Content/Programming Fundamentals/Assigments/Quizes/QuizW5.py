## 1 ## Select the expression that evaluates to True
len('mom') in [1,2,3]
#True
len([1,2,3]) == len(['a','b','c'])
#True
'a'in['mom','dad']
#False
int('3')in[len('a'),len('ab'),len('abc')]
#True
'3'in[1,2,3]
#False
[1, 2, 3] in len('mom')
#TypeError: argument of type 'int' is not iterable

## 2 ## Consider this code and select the function calls that result in error.
def mystery(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1
   
    return result
help(str.isdigit)

mystery('abc123')
#'' 
mystery('123abc')
#'123'
mystery('123')
#IndexError: string index out of range
mystery('abc')
#''
#That one results in error because we don't have a paratemer that tells the while loop to stop when the end of the string is reached.

## 3 ## Consider this code and select the best description for the function
def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result
#Return a list containing every third item from L starting at index 0.
#That's the best choice because it tells what's the argument and what the function does.
#The key point here is that it sais "returns third item" and that's the most appropiate description since
#it is a list and the values inside a list are all called items.

## 4 ## Select the missing line of code
def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements       
    from Lconcatenated together, starting with indices 0 and 1,    
    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE

     return compressed_list

#i=i+i
#i=i+2 <---> This one because we want to step to the next character that comes after the ones we already grouped.
#i=i+1
#i=i*2

## 5 ##
#What is the sum of the even numbers from 524 through 10508, inclusive? 
#Hint: write a while loop to accumulate the sum and print it. Then copy and paste that sum. For 
#maximum learning, do it with a for loop as well, using range.

nums = 524
acc = 0
while nums <= 10508:
    acc = acc + nums
    nums = nums + 2
print(acc)

## 6 ## Consider this code:
def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
          i = i + 1

     return total
#The while loop stops as soon as an even number is found, and the sum of all the previous numbers is returned.
#The four functions below use a for loop to try to accomplish the same task, although 
#they keep iterating through all of the numbers in L regardless of whether the numbers are even or odd. 
#Only one of them returns the same value as function while_version. Which one is it?
"for_version([1, 3, 5, 6, 7, 9, 10])"
def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total
#25
#TypeError: 'function' object is not subscriptable
def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total
#9 - > This one because it keeps adding the number if % 2 != 0. If else found_even = True and 
#then when it reaches the for loop again, "and not found_even" will be false and the for loop will not execute.
 
def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
            found_even = True

    return total
#25
def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total
#25

## 7 ##
numbers = [1, 4, 3]
#MISSING CODE HERE
print(numbers)
#[3, 4, 1]

#Which of the following code fragments(s) could be the missing code in the program above?
reverse(numbers)
numbers.reverse() #This one, because is the correct list.method()
reverse(numbers)
numbers=numbers.reverse()

## 8 ## What is printed by the following code?
fruits = ['banana', 'apple', 'pear', 'peach']
fruits.insert(fruits.index('pear'), 'watermelon')
print(fruits)

#[’banana’,’watermelon’,’apple’,’pear’,’peach’]
#[’banana’,’apple’,’watermelon’,’peach’]
#[’banana’,’apple’,’watermelon’,’pear’,’peach’] <- This one, because it enters at the second index and slices the other items.
#[’banana’,’apple’,’pear’,’watermelon’,’peach’]

## 9 ##
playlist = ['Lola','Venus','Lola','Lola','LetItBe','Lola','ABC','Cecilia','Lola','Lola']
#You want to make sure that Lola gets played at most 3 times, so you want to complete this function that edits the playlist:

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    cap_song_repetition(['Lola','Venus','Lola','Lola','LetItBe','Lola','ABC','Cecilia','Lola','Lola'], 'Lola')
    '''

    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))
    return playlist
#Select the loop(s) that accomplish this.
help(str.index)

while playlist.count(song) > 3:
        playlist.pop(playlist.index(song)) 
#['Venus', 'LetItBe', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
while playlist.count(song) > 3:
        playlist.pop(song)
#TypeError: 'str' object cannot be interpreted as an integer  
help(list.pop)
#song = str != list.pop() --> argument = int, not str. 
while playlist.count(song) > 3:
        playlist.remove(song)
#['Venus', 'LetItBe', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']
help(list.remove)
#song = str == list.remove() --> argument = value = str = item
while playlist.count(song) >= 3:
        playlist.remove(song)
#['Venus', 'LetItBe', 'ABC', 'Cecilia', 'Lola', 'Lola']
#Ii said "at most 3 times" this still valid because >= 3 means less than 3 times, which still acomplishing the "at most 3 times" parameter.
while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))
#ValueError: list.remove(x): x not in list
#song = index != list.remove() --> argument = value. If value not in list = ValueError

## 10 ## Consider this code 
a = [1, 2, 3]
b = a
a=[1,'A',3]
b=[1,'A',3]    # MISSING CODE HERE
print(a, b)
#[1, 'A', 3] [1, 'A', 3]
#Which of the following code fragments(s) could be the missing code in the program above?

b[1]='AB'
#[1, 'AB', 3] [1, 'AB', 3] Wrong -> modifying list at index 1 with 'AB', not 'A'
a[1]=a[1][0]
#TypeError: 'int' object is not subscriptable
#[1, 2, 3] [1, 2, 3] Wrong -> doesn't modify the list because of the TypeError in attempt to modify the list.
a[1]='A'
#[1, 'A', 3] [1, 'A', 3] Right -> modifying list at index 1 with 'A'  
a=[1,'A',3]
#[1, 'A', 3] [1, 2, 3] Wrong -> modifying variable a will assign a new value to the varaible but wont modify the list.
b=[1,'A',3]
#[1, 2, 3] [1, 'A', 3] Wrong -> modifying variable b will assign a new value to the varaible but wont modify the list.
b[-2]='A'
#[1, 'A', 3] [1, 'A', 3] Right -> modifying list at index -2 with 'A'. [-2] = [1]
a=[1,'A',3]
b=[1,'A',3]
#[1, 'A', 3] [1, 'A', 3] Right -> modifying both values will assign new values to each one,
# and the values that we assigned are the ones that we want. 

## 12 ## What is printed by the following code?
def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
#None -> It prints None because the there is not return statement to the function inside the print(function)
print(values)
#[3, 4, 5] -> variables aren't mutable BUT lists are mutable, then it prints the list that has been modified that is assigned to the variable.

## 13 ## Select the code fragment(s) that print [3,6,9].
values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)
#[3, 6, 9] -> range(10) not inclusive, but 9 is included so it is printed.
values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)
#[3, 6, 9] -> range(1, 4)(num*3) = range(3, 12, 3) -> because default step = 1
values = []
for num in range(3, 9, 3):
    values.append(num)
print(values)
#[3, 6] -> range(9) NOT inclusive, so it prints only 3, 6. 
values = []
for num in range(1, 3):
    values.append(num * 3)
print(values)
#[3, 6] -> (1, 3)(num*3) = 3, 9, 3 -> since not inclusive, it only prints until 6.

## 14 ##Select the function calls to range
for num in range(x,y,z):
    print(num)
#That produces the following output:
3
11
19
# Answer: It should contain at least: start. index = 3; range = > 19 step = 8
range(3,19,8)
#3
#11
range(3,8,20)
#3
range(3,20,8)
#3
#11
#19
range(3,23,8)
#3
#11
#19








