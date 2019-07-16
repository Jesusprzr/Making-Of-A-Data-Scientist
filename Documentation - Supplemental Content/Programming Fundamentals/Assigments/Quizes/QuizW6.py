
#TODO: Passed the exam (11/13). But should check answers 3 and 12 because both are wrong. 
#? 1- What is printed by the following code?
def merger(L):
    merger = []
    for i in range(0, len(L), 3):
        merger.append(L[i] + L[i + 1] + L[i + 2])
    return merger

print(merger([1,2,3,4,5,6,7,8,9]))
#//[123,456,789] 
#//[12,15,18]
#//[1,4,7]
#!These are NOT the answer because we are summing ints, not only appending. 
#!We are starting at index 0, not the number 3, which is index 2.
#!We are NOT only appending the item at index [i]. Before appending we are also doing the aritmethic operation:  L[i] + L[i + 1] + L[i + 2].
#*[6, 15, 24]  
##This is printed because we are appending a list of ints. Remember that you can do aritmethic operations even with different types!
##We have a step of three so we go from L[0] = 1, to L[3] = 4 and finally to L[6] = 7. On every idnex we sum = L[i] + L[i + 1] + L[i + 2].
#TODO: I choosed the wrong answer here, so gotta do some examples that result in the different outcomes.

#? 2- Trace the function call mystery(’civil’) on the following code using the Python Visualizer. How many times is the line marked reached?
def mystery(s):
    """(str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: #? how many times this line is reached?
            matches = matches + 1
    return matches == (len(s) // 2)
mystery('civil')
#*2
##Basically we could have known that just by the loop "for i in range(len(s) // 2):" becuase it is the only statement that infers into how
##many times the inner loop will be reached. And the inner loop only executes once every time is reached so it isn't relevant. 

#? 3- Consider the function above. Which is the best docstring description for function mystery(s):
#Some examples to understand the function:
mystery('beeb')
mystery('beev')
mystery('beveb')
mystery('beeeeeeeb')

#// Return True if and only if there are exactly len(s) // 2 characters in s that are the same character.
#! This one is discarted because it states that half of the characters are the same.
#* Return True if and only if the number of duplicated characters in s is equal to len(s) // 2.
## I'm going with this one because it states that the duplicated characters in s are equal to the half of s.
#// Return True if and only if s is equal to the reverse of s.
#! This one is discarted because it tells what the function does but not how.
#// Return True if and only if s[len(s) // 2] is the same as s[len(s) // 2:]
#! This one is discarted because doesn't make that muchs sense at all.

#? 4- Consider the function shift right:
def shift_right(L):
    """ Arguments:
        L (list) -- NoneType
        Summary:
        Shift each item in L one position to the right and shift the last item to the first position.
        Precondition:       
        Len(L) >= 1
    """
    last_item = L[-1]

    #// Missing code

    L[0] = last_item
#? Select the code line that correctly completes the function:

for i in range(len(L) - 1):
    L[i] = L[i + 1]
#! wrong because we would be shifting left.
for i in range(len(L)):
    L[i + 1] = L[i]
#! Wrong because we are calling an index out of range to substitude its value for our L[-1].
for i in range(1, len(L)):
    L[i] = L[i + 1]
#! Wronng because yes, range is correct. But the substitution is to the left and we also would get an out of range index error.
for i in range(1, len(L)):
    L[len(L) - i)] = L[len(L) - i - 1]
#* This one is correct because the range is correct and we are substituting backwards. From last to first and to the right. 

#? 5- Consider the following code (now docstrings get a little tough to write!):
def make_pairs(list1, list2):
    """ (list of str, list of int) -> list of [str, int] lists.
    Return a nwe list in which each item is a 2-item list ith the string from the corresponding position 
    of list1 and the int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)    

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    """
    pairs = []

    #// Missing code

    return pairs

#? Select the code fragment(s) that mamkes the function match its description:
inner_list = []
    for i in range(len(list1)):
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
#// [['A', 1, 'B', 2, 'C', 3], ['A', 1, 'B', 2, 'C', 3], ['A', 1, 'B', 2, 'C', 3]]
#! Here having the inner_list outside the loop causes it to append all pairs 3 times for every iteration of the loop.
for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])
#* [['A', 1], ['B', 2], ['C', 3]]
## This works perfect because with little code we create one inner list every time we iterate through the range. 
for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
#* [['A', 1], ['B', 2], ['C', 3]]
## Here our inner list is inside the loop, so everytime we iterate through the loop we are creating a new inner_list and adding the pairs.
for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
    pairs.append(inner_list)
#// [['C', 3]]
#! This one doesn't works because it iterates perfectly through the loop but since pairs.append is outside the inner list append
#! We add only the last iteration. 

#? 6- Consider the following code:
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Using values and indexing with non-negative indices, write an expression that evaluates to 5. 
#Do not use addition, subtraction, or parentheses () ([] are required).
#* values[1][1]

#? 7- Consider the following code:
breakfast = [['French', 'toast'], ['blueberry', 'pancakes'], ['scrambled', 'eggs']]
#Using breakfast and indexing with only negative indices, write an expression that evaluates to ’blueberry’. 
# Do not use addition, subtraction, or parentheses () ([] are required).
#* breakfast[-2][-2]

#? 8- Consider the following code:
for i in range(2, 5):
    for j in range(4, 9):
        print(i, j)
#? Trace the code above in the Python Visualizer. How many times is print(i,j) executed?
#* 15
## You could do it without the visualizer by understanding how the loops and ranges execute.
## i in range(2,5) = 3 exections. j in range(4, 9) = 5 executions. Since inner loop completely executes each time the outer loop
## executes then 3*5 = 15.

#? 9- Consider the following code:
def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False  # We have not yet found value in the list.

    #// CODE MISSING HERE
   
    return found

#? Select the code fragment(s) that make the function above match its docstring description.

 for sublist in lst:
        if value in sublist:
            found = True
#* True
## the loops evaluate each sublist in list, if value in sublist found = True. So it does it's function correctly.
for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
#* True
## Here is the same as above but with ranges. we evaluate for each j in the range of items of the current list. If value == j. found = True
for item in lst:
        if value == item:
            value = True
#! False
#! This is false because we are not evaluating each item in each sub-list, instead we are just evaluating the entire sub-list as a whole.
for i in range(len(lst)):
        for j in range(len(lst[i])):
            found = (lst[i][j] == value)
#! False
#! This is false because it will iterate through the list evaluating the found state for each j in range(len(lst)).  

#? 10- You want to write a program that prints the average of the high temperatures in January. 
''' File example:
Preamble line
\n
January temperature line
February temperature line
March temperature line
...
December temperature line
Thousands of lines of information that we aren't interested in.
End onf the file. 
'''
#? Which of the four file-reading approaches should you use?

#*I think the readline approach is the most convenient because we want to get to January which is at the top and only use that data.
#* Therefore the readline approach is the one which would get us there more efficiently. 
#! I am not choosing something like the readlines approach because yes, it is good because it indexes the lines but i don't want 
#! a huge string made up of thousands of lines that I don't care about, i just want one line that's near the top.

#? 11- Consider the following code:
# data_file refers to a file open for reading.
for line in data_file:
     print(line)
#? Select the code fragment(s) that when used as replacement(s) for print(line) will print the lines without extra blank lines.
print(line.strip())
    help(str.strip)
    #Return a copy of the string with leading and trailing whitespace remove.
#! This may work because removes trailing withespaces. But also removes leading so it wont.
print(line-'\n')
#! This one won't work bacuse it will delete the spaces only when we fint a blank line.
print(line.rstrip(’\n’))
    help(str.rstrip)
    #Return a copy of the string with trailing whitespace removed.
#* This one should remove the blank lines in the file.
print(line,end='')
#* I know this one is correct because the print will execute until it finds no more code in the line.

#? 12- Consider the following code:
def lines_startswith(file, letter):
     """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.     
     The lines should have the new line removed.

    Precondition: len(letter) == 1
    """

    matches = []

    #// CODE MISSING HERE

    return matches
#? Select the code fragment(s) that make the function above match its docstring description.

for line in file:
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))
#* This one should work because it will iterate throught the file and append the line that starts with letter to matches.
for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
#! This one wont work because it says line[0] so if line starts with letter but it has a word at index 0 it will equally be false.
matches.append(line.startswith(letter).rstrip('\n'))
#! The function is correct but it doesn't have any parameter that makes it iterate throught the entire file.
 for line in file:
        if letter in line:
            matches.append(line.rstrip('\n'))
#! This wont work because it will just append every letter in the file to matches.

#? 13- Consider the following code:
def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE MISSING HERE
#? Select the code fragment(s) that make the function above match its docstring description.

file.write(sentences)
#! This one looks good but the think is that is not adding each sentence in different lines.
for s in sentences:
        file.write(s)
        file.write('\n')
#* This one should work because for each line it will write s and then \n to go to the next line.
for s in sentences:
        file.write(s + '\n')
#* This one should work because on each line it will write the sentence and the \n to go to the next line.
for s in sentences:
        file.write(s)
    file.write('\n')
#! This one wont work because it will write the sentence and then on a new line \n.
for s in sentences:
        file.write(s)
#! Not sure if this one would work because it will write on the file every sentence but nothing else.
