# Python Syntax Cheatsheet

## Code Layout
* Line endings separate statements. Semicolons optional.
* Consecutive lines indented with same number of spaces form a block
* Line comments begin with `#`.
* No block comments, but triple quoted strings can be used instead

## Operators
* Arithmetical: `+`,`-`,`*`,`/`,`//` (integer division),`%`,`**` (exponent)
  * and their *compound assignment* counterparts: `+=`,`-=`,`*=`,`/=`,`//=`,`%=`,`**=`
* Comparison: `==`,`!=` (or `<>`),`>`,`>=`,`<`,`<=`
* Bitwise: `&` (and), `|` (or), `^` (xor), `~` (not), `<<`, `>>`
* Boolean: `and`, `or`, `not`
* Membership: `in`, `not in`
* Identity: `is`, `is not`

## Variables
### Variables vs constants
Python has no constants, but variables named in ALL_CAPS should be treated as constants by convention.
```python
age = 15            # variable
PI = 3.1415926      # pseudo-constant
```
### Assignment
- Assigment: `x = 1`
	- Simultaneous assignment: `z = y = x = 1`
- Multiple assignment: `x,y,z = 1,2,"john"`
	- Unpacking: `x,y,z = [1,2,"john"]`

### None
The keyword `None` represents Python's null value, e.g. `x = None`

## Built-in Types
### Built-in data types
#### Scalars
- Number: `1` (int), `1.27` (float), `1+3j` (complex)
	- int representations: `0o77` (octal), `0xFF` (hexadecimal)
- String: `'john', '''john''', "john", """john"""`
- Boolean: `True`, `False`

#### Collections
- Ranges: `range(start, end, step)`
	- `range(10)` #=> 1, 2, 3, ..., 9
	- `range(0,100,5)` #=> 0, 5, 10, 15, ..., 90, 95
- Lists: `[1, 18, 'john']`
- Tuples: `(1, 18, 'john')`
- Sets: `{1, 18, 'john'}`
- Frozensets:  `frozenset({1,18,'john'})`
- Dictionaries `{'id': 1, 'age': 18, 'name': 'john'}`

|         | List | Tuple | Set | Frozenset |
|---------|:-----:|:------:|:----:|:----------:|
| Mutable |   ✅   |    ❌   |   ✅  |      ❌     |
| Ordered |   ✅   |    ✅   |   ❌  |     ❌     |

Trailing commas in collection literals are ignored, e.g. `[1,2,3,]`

### Strings
- Enclosed in single quotes (`'john'`) or double quotes (`"john"`)
- Triple-quoted strings supported for multiline strings: `'''multiple lines here'''`
- String interpolation / Formatted string literals (f-strings): `f'Hello {name}. The answer is {41 + 1}'`
- String formatting operator: `'Hello %s! The answer is %d' % (name,41+1)`

#### String concatenation
The following examples all return `'helloworld'`:
- `'hello' + 'world'`
- `'hello''world'`
- `('hello' 'world')`

### Iterables
An *iterable* is any object capable of returning its elements (members) one at a time (e.g. in a `for` loop). Iterable types include:
- strings
- collections: lists, tuples, sets, dictionaries

The *slice operator* `[]` works with all iterables:
- `iterable[n]`: element at position `n`
	- Index starts at `0`
	- Negative position is relative to the end, `-1` indicating the last element
- `iterable[m:n]`: elements between positions `m` and `n`.
	- Either `m` or `n` may be omitted.
- `iterable[m:n:s]`: elements between positions `m` and `n` with step `s`

The following built-in fuctions act on iterables:
- `len(x)`
- `sum(x)`
- `max(x)`, `min(x)`
- `any(x)`, `all(x)`
- `sorted(x)`
- `enumerate(x)`

The following operators work with some iterables, such as strings, lists and tuples:
- `+` for concatenation: `[1,2,3] + [4,5,6]`
- `*` for repetition: `[1,2,3] * 3`

### Iterable comprehensions
Iterables can be mapped and/or filtered with the following general syntax:
```python
[ map(member) for member in _list if filter(member) ]
{ map(member) for member in _set if filter(member) }
{ map(key): map(value) for key, value in _dict.items() if filter(key, value) }
```

### Data type conversions
There are several built-in functions to perform conversion between compatible data types. These functions return a new object representing the converted value.

- String conversions:
  -  `str(x)` (informal string representation)
  -  `repr(x)` (formal string representation)
- Number conversions: `int(x, base)`, `float(x)`, `complex(x, i)`, `oct(x)`, `hex(x)`
- Boolean conversion: `bool(x)`
- Character conversions: `chr(x)` <--> `ord(x)`
- Iterable type conversions: `list(s)`, `tuple(s)`, `set(s)`

## Control Statements
### Conditions
```python
if condition:
  pass
elif condition:
  pass
else:
  pass
```
#### Ternary operator
`'kid' if age < 18 else 'adult'`

### Named tuples
```python
from collections import namedtuple  
Variable = namedtuple('Type',['keyname1','keyname2','keyname3']) 
```
#### Named tuples import
`from collections import namedtuple` is necessary for using named tuples.
Named tuples were added in python 2.6, although there is a recipe for implementation in Python 2.4.(https://code.activestate.com/recipes/500261/)
### Loops
```python
while condition:
  pass
```
```python
for element in iterable:
  pass
```
#### Loop control statements
- `break`: Terminate the loop
- `continue`: Skip the remainder of this iteration

### Exceptions
#### Handling exceptions
```python
try:
  # ...
except error_type_1:
  # handle error_type_1
except error_type_2 as err:
  # handle error_type_2, assigned to variable err
except (error_type_2, error_type_3):
  # handle error_type_2, error_type_3
except (error_type_2, error_type_3):
  # handle error_type_2, error_type_3
except:
  # handle all other errors
finally:
  # clean-up code to run always at the end,
  # whether an error wasd encountered or not
```
#### Raising exceptions
```python
raise                                 # raise RuntimeError
raise ValueError                      # raise ValueError
raise ValueError('not an integer')    # raise ValueError: not an integer
```
#### Raising assertion errors
```python
assert 3 + 1 == 4                     # does nothing
assert 3 + 1 == 5                     # raises AssertionError
assert 3 != 0, 'should not be zero'   # raises AssertionError: should not be zero
```

## Files
### Reading from a file
```python
# Without context manager
f = open("file.txt")
for line in f:
  pass
f.close()
```
```python
# With context manager, file closes automatically at the end
with open("file.txt") as f:
  for line in f:
    pass
```
## Functions

Python allows defining named as well as anonymous (lambda) functions:
- Both named and lambda functions can be assigned to variables or passed as arguments
- Lambda definitions are limited to one statement

```python
# Named function
def add(x, y):
  return x + y

# Lambda function
add = lambda x, y: x + y
```

### Nested functions

```python
def filter_adults(people):
  def is_adult(person):
    return person.age >= 18
  return [person for person in people if is_adult(person)]
```

### Function arguments
- Function arguments can optionally have default values: `def print_headline(width=1)`
- Functions may accept:
	-  an indefinite number of positional arguments: `def func(*args)`
	-  an indefinite number of keyword arguments:  `def func(**kwargs)`

```python
def func(first, second, *rest, option1 = True, option2 = 'yes', **options):
  print(f"{first=}  {second=}  {rest=}")
  print(f"{option1=}  {option2=}  {options=}")

func(12, 23, 34, 35, 56, option3 = 'maybe', option2 = 'no', option4 = False)
#=> first=12  second=23  rest=(34, 45, 56)
#=> option1=True  option2='no'  options={'option3': 'maybe', 'option4': True}
```

- The caller may specify arguments
  - either by position or by keyword
  - either unpacked or packed

```python
def func(first, second):
  print(f"{first=}  {second=}")

# All of the calls below are equivalent:
func(1, 2)
func(1, second = 2)
func(first = 1, second = 2)
func(second = 2, first = 1)

# args are unpacked by position from a list
args = [1,2]
func(*args)

# args are unpacked by keyword from a dictionary
args = {'first': 1, 'second': 2}
func(**args)

# The following call throws an error
func(1, first=1)
#=> TypeError: func() got multiple values for argument 'first'
```

## Modules and Packages
- **Script:** A python source file meant to be executed directly
- **Module:** A python source file meant to be imported rather than executed directly
- **Package:** A directory of related modules, including a special `__init__.py` script
