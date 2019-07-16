"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    valid = False
    for words in wordlist:
        if words == word:
            valid = True
    return valid


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    row_string = ''
    for character in board[row_index]:
        row_string += character
    return row_string


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    col_string = ''
    for sublist in board:
        col_string += sublist[column_index]
    return col_string

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TB')
    True
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'AX')
    True
    """
    lst = board[0]
    for column_index in range(len(lst)):
        if word in make_str_from_column(board, column_index):
                return True

    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    if board_contains_word_in_column(board, word):
        return True
    if board_contains_word_in_row(board, word):
        return True
    else:
        return False


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    score = 0
    word_count = 0
    for l in word:
        word_count += 1
    if word_count in range(1, 3):
        score = 0
    if word_count in range(3,7):
        score += word_count * 1
    if word_count in range(7, 10):
        score += word_count * 2
    if word_count >= 10:
        score += word_count * 3    
    
    return score

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    t_score = player_info[1]
    player_info[1] = t_score + word_score(word)



def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    num_words = 0
    for word in words:
        if board_contains_word_in_column(board, word):
            num_words += 1
        if board_contains_word_in_row(board, word):
            num_words += 1
    return num_words

def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    
    new_list = []
    lst = words_file.readlines()
    for i in lst:
        if i != '\n':
            new_list.append(i)
    return new_list

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    
    board = []
    sub_board = []
    for line in board_file:
        for i in range(0, len(line) - 4, 5):
            sub_board += i[i]+ i[i + 1] + i[i + 2] + i[i + 3]
        board += sub_board     
        return board

'''Some tests failed:
[TestBoardContainsWordInColumn] Your code raised an unexpected exception: list index out of range
[TestBoardContainsWordInColumn] Your code raised an unexpected exception: list index out of range
[TestBoardContainsWord] Your code raised an unexpected exception: list index out of range
[TestBoardContainsWord] Your code raised an unexpected exception: list index out of range
[TestBoardContainsWord] Your code raised an unexpected exception: list index out of range
[TestReadBoard] Your code raised an unexpected exception: No module named '_tkinter', please install the python3-tk package
[TestReadBoard] Your code raised an unexpected exception: No module named '_tkinter', please install the python3-tk package
[TestReadBoard] Your code raised an unexpected exception: No module named '_tkinter', please install the python3-tk package
[TestReadBoard] Your code raised an unexpected exception: No module named '_tkinter', please install the python3-tk package
[TestReadWords] Your code raised an unexpected exception: No module named '_tkinter', please install the python3-tk package
[TestReadWords] Your code raised an unexpected exception: No module named '_tkinter', please install the python3-tk package
[TestReadWords] Your code raised an unexpected exception: No module named '_tkinter', please install the python3-tk package
'''