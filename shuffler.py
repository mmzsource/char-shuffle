from sys import argv
import random

def shuffle(line):
  """Loops the shuffler over all words in a line"""
  shuffled_line = ''
  for i in split_line(line):
    shuffled_line += shuffle_inner_chars(i) + ' '
  return shuffled_line

def split_line(line):
  """Splits a given sentence into a sequence of words"""
  return line.split(' ')

def shuffle_inner_chars(word):
  """Shuffles all characters of a word except the first and the last character"""
  if len(word) < 4:
    return word

  first_char = word[:1]
  last_char = word[-1:]
  middle = word[1:-1]
  middle_chars = ''.join(random.sample(middle, len(middle)))
  return first_char + middle_chars + last_char

def main():
  """Loops over all lines in the file specified in the run argument. Expects a text file"""

  if len(argv) == 2:
    with open(argv[1]) as f:
      lines = f.read().splitlines();
      for line in lines:
        print shuffle(line)
  else:
    print "This script expects a path to a textfile as a commandline argument"

if __name__ == '__main__':
  main()

