#FINAL EXAM
#? 1- Select the expression that evaluates to int:
8 % 6       #*
8.0 % 4     #! Yes but not, the result is 8.0 
8 + 3       #*
7 + 8.5     #!

#? 2- Consider the following code:
a = 7
b = a + 3
a = 9
#? What does b refer to?
10

#? 3- Consider this code:
def f(x):
    y = x*3
    return y - x
#? What value is returned on a call f(10)?
20

#? 4- write an expression that evaluates to 'L8R' (do not use unnecessary parentheses) with the following code:
start = 'L'
middle = 8
end = 'R'

start + middle.__str__() + end

#? 5- Consider this function:
def larger_of_smallest(L1, L2):
    ''' (list of int, list of int) -> int

    Return the larger of the smallest value in L1 and the smallest value in L2.

    Precondition: L1 and L2 are not empty.

    >>> larger_of_smallest([1, 4, 0], [3, 2])
    2
    '''
    return #//Missing code
#? write the missed expression. use only 1 max and 2 min. Do not use unnecessary parentheses.
#* max(min(L1), min(L2))

#? 6- Consider this code:
def same_lenght(L1, L2):
    ''' (list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    '''
    if len(L1) == len(L2):
        return True
    else:
        return False
#? It works, but the if is unnecessary, write a one-line return expression:
#* return len(L1) == len(L2)

#? 7- Consider these two incomplete functions:
def moogah(a, b):
    ''' (str, int) -> str'''

def frooble(L):
    ''' (list of str) -> int
    Precondition: L has at least one element. '''
#? Select the code fragments that are valid according to the function headers and type contracts.
lst = ['a', 'b', 'c']
moogah(lst[0], len(lst))
#* (a,b) -> (str,int) == (lst[0], len(lst))
moogah('a', moogah(['a']))
#! (a,b) -> (str,int) != (str, moogah(list)) + moogah needs two arguments (str, int).
moogah(frooble(['a']), 'a')
#! (a,b) -> (str,int) != (int, str)
moogah('a', frooble(['a']))
#* (a,b) -> (str,int) == (str, frooble(['a'])) -> frooble(['a']) will translate into an int.

#? 8- Consider this code:
def gather_every_nth(L, n):
    ''' (list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''
    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = #// Missing code
    return result
#? Write the missing expression without (). 
#* i + n

#? 9- Consider the following code:
def get_keys(L, d):
    ''' (list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2,'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for #// Missing code
        if k in L:
            result.append(k)
    return result
#? Write the missing code, do not use () or functions or methods.
#* k in d: because k is item in the dictionary, so what we are saying is that for item in d, if item in l, result.append(item)
#TODO: Practice this a lil more, because didn't get to the answer on the first attempts. 

#? 10- Consider this code:
def are_lenghts_of_strs(L1, L2):
    ''' (list of int, list of str) -> bool

    Return True if and only if all the ints in L1 are the lengths of the strings.

    Precondition: len(L1) == len(L2).

    >>> are_lenghts_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True 
    '''
    result = True
    for i in range(len(L1)):
        if L1[i] != len(L2[i]): #// Misiing code 
            result = False
    return result
#? Write the missing code. Answer should be of the form: expr1 != expr2:; Use only variables i, L1, L2 , indexing and function len.
#* L1[i] != len(L2[i]): because we are executing the loop len(L1) times, and we want to compare each item in L1 with the lenght of
#* its corresponding item in L2. So we use index L1[i] and index L2[i] so the index will be the same.

#? 11- Consider this incomplete function:
def double_last_value(L):
    ''' (list of int) -> NoneType

    Double the value at L[-1]. For example, if L[-1] is 3, replace it with 6.

    Precondition: len(L) >= 1.
    '''
#? and this code:
L1 = [1, 3, 5]
double_last_value(L1)
print(L1[-1])
#? Enter the printed number
#* 10

#? 12- Consider this function:
def get_negative_nonnegative_lists(L):
    ''' (list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the 
    inner lists of L and the second item is a list of the non-negative ints 
    in those lists. 

    Precondition: the number of rows in L is the same as the number of columns. 

    >>> get_negative_nonnegative_lists([[-1, 3, 5], [2, -4, 5], [4, 0, 8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''
    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
             #// Missing code start
            if L[row][col] < 0:
                neg.append(L[row][col])
            
            nonneg.append(L[row][col])
            #// Missing code end           
    return (neg, nonneg)
#? Select the code fragment(s) that correctly complete this function.
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)
#* This one does it perfectly, because it evaluates every nested item and appends it to the corresponding 0 > or < 0 list.
            if L[row][col] > 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])
#! This one does everything perfect, except for one and only one thing. Since nonneg.append is for values > 0. It will 
#! exclude the value 0 when appending values to the list and because of else: it will append it to the negative list.
            if L[row][col] < 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])
#! Totally wrong, it will end up doing the opossite of what is wanted. It will append < 0 to nonneg and > 0 to neg. 
            if L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])
#* Correct, because it will append the numbers that are < 0 to neg and every other number (including 0) to nonneg.
            if L[row][col] < 0:
                neg.append(L[row][col])
            
            nonneg.append(L[row][col])
#! It will do its job on appending the negative numbers to neg. BUT it will append each and every number to the
#! nonneg list, and just because nonneg.append is at the same level of statement and has no statement. 

#? 13- Consider this code:
def add_to_letter_counts(d, s):
    ''' (dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    {'i': 1, 'r': 6, 'e': 4}
    '''
    for c in s:
        #// Missing code
#? Write the missing statement. Do not call any functions or methods. 
d[c] = d[c] + 1 
#TODO: Took me a while to get to the answer, at the end it made sense to me but gotta practice and transcript the lesson to
#TODO: really understand what is going on under the hood and what works and what doesn't. 
#TODO: Answer from question 4 is wrong, gotta check. 
