Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 12 * 20 / 2
120.0
>>> base = 20
>>> height = 12
>>> base * height /2
120.0
>>> base
20
>>> height
12
>>> area = base * height / 2
>>> area
120.0
>>> base = 10
>>> height = 20
>>> area = base * height / 2
>>> area
100.0
>>> 10 * 20 / 2
100.0
>>> base 1 = 10
SyntaxError: invalid syntax
>>> base_1 = 10
>>> base_2 = 35
>>> Base_3 = 10
>>> Bas_4 = 35
>>> perimeter = base_1 + base_2 + base_3 + base_4
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    perimeter = base_1 + base_2 + base_3 + base_4
NameError: name 'base_3' is not defined
>>> base_3 = 10
>>> base_4 = 35
>>> perimeter = base_1 + base_2 + base_3 + base_4
>>> perimeter
90
>>> max(1.40, 30.78, 20.5, 103)
103
>>> max(perimeter, area, base, height)
100.0
>>> dir
<built-in function dir>
>>> dir
<built-in function dir>
>>> dir(__buildins__)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dir(__buildins__)
NameError: name '__buildins__' is not defined
>>> dir(_buildins_)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dir(_buildins_)
NameError: name '_buildins_' is not defined
>>> dir(___buildins___)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dir(___buildins___)
NameError: name '___buildins___' is not defined
>>> dir(_builtinds_)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dir(_builtinds_)
NameError: name '_builtinds_' is not defined
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> help(abs)
Help on built-in function abs in module builtins:

abs(...)
    abs(number) -> number
    
    Return the absolute value of the argument.

>>> abs(-45)
45
>>> help(pow)
Help on built-in function pow in module builtins:

pow(...)
    pow(x, y[, z]) -> number
    
    With two arguments, equivalent to x**y.  With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for ints).

>>> def f(x):
	return x ** 2
f(3)
SyntaxError: invalid syntax
>>> f (3)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    f (3)
NameError: name 'f' is not defined
>>> def f(x):
	return x ** 2

>>> f(3)
9
>>> x
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> y = 5
>>> f(y)
25
>>> def increment(z)
SyntaxError: invalid syntax
>>> def increment(z):
	return z + 10

>>> increment(90)
100
>>> increment(y)
15
>>> result = f(y)
>>> result
25
>>> def T_area(base, height):
	return base * height / 2

>>> T_area(10, 20)
100.0
>>> T_area(3, 4)
6.0
>>> 
