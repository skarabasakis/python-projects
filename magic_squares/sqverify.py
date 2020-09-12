def load_square(input):
  return [[int(n) for n in line.split()] for line in input.splitlines()]

def row(square, index):
  return square[index]

def col(square, index):
  return [line[index] for line in square]

def diag(square, reverse = False):
  index_list = list(range(len(square)))
  if reverse:
    index_list.reverse()
  return [square[x][y] for x, y in enumerate(index_list)]

def is_square(square):
  return all([len(square) == len(row) for row in square])

def has_no_repeating_elements(square):
  elements = [element for row in square for element in row]
  return len(set(elements)) == len(elements)

def is_magic(square):
  lines = [
    *[row(square, n) for n in range(len(square))],
    *[col(square, n) for n in range(len(square))],
    *[diag(square, n) for n in [True, False]]
  ]
  sums = [sum(line) for line in lines]
  return len(set(sums)) == 1

def is_magic_square(square):
  return is_square(square) and has_no_repeating_elements(square) and is_magic(square)

def print_message(is_magic_square):
  if is_magic_square:
    print("Input is magic square")
  else:
    print("Input is not magic square")

stdin = open('square.txt')
square = load_square(stdin.read())
print(is_magic_square(square))
