import unittest
from shuffler import *

class TestShuffler(unittest.TestCase):

  def setup(self):
    pass

  def test_should_split_a_line_into_words(self):
    self.assertEquals(split_line("This is a line"), ["This", "is", "a", "line"])

  def test_should_split_an_empty_line_into_a_list_with_one_empty_element(self):
    self.assertEquals(split_line(""), [""])

  def test_should_leave_number_of_characters_intact(self):
    abc = "abcdefghijklmnopqrstuvwxyz"
    self.assertEquals(len(shuffle_inner_chars(abc)), len(abc))

  def test_should_leave_first_character(self):
    self.assertEquals(shuffle_inner_chars("a")[0], 'a')
    self.assertEquals(shuffle_inner_chars("klm")[0], 'k')
    self.assertEquals(shuffle_inner_chars("xyz")[0], 'x')
    self.assertEquals(shuffle_inner_chars("blahblahblah")[0], 'b')
    self.assertEquals(shuffle_inner_chars("foobar")[0], 'f')

  def test_should_leave_last_character(self):
    self.assertEquals(shuffle_inner_chars("a")[-1], 'a')
    self.assertEquals(shuffle_inner_chars("klm")[-1], 'm')
    self.assertEquals(shuffle_inner_chars("xyz")[-1], 'z')
    self.assertEquals(shuffle_inner_chars("blahblahblah")[-1], 'h')
    self.assertEquals(shuffle_inner_chars("foobar")[-1], 'r')

  def test_should_shuffle_middle_characters(self):
    # There is a chance this test fails while the code works
    # The chance that the code will shuffle 'word' to 'wrod' is 50% (assuming shuffling works randomly)
    # The chance it will change 'word' to 'wrod' at least one time in 100 tries is 1 - (0.5**100) which is ~ 1
    result = []
    for i in range(100):
      result.append(shuffle_inner_chars("word"))
    self.assertTrue("wrod" in result)

  def test_should_leave_number_of_words_intact(self):
    line = "This line contains five words"
    shuffled_line = shuffle(line).strip()
    self.assertEquals(len(shuffled_line.split(' ')), len(line.split(' ')))
    

if __name__ == '__main__':
  unittest.main()
