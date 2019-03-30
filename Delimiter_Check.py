import sys
from Stack import Stack

def delimiter_check(filename):
  stack = Stack()
  with open(filename, 'r') as file:
    file_chrs = list(file.read())
  for char in file_chrs:
    if any([ char == '(', char == '{', char == '[' ]) == True:
      stack.push(char)
    elif (char == ')' and stack.pop() != '(') or (char == '}' and stack.pop() != '{') or (char == ']' and stack.pop() != '['):
      return False
  return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')
