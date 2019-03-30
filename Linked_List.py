class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      self.val = val
      self.next = None
      self.prev = None

  def __init__(self):
    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__size = 0

  def __len__(self):
    return self.__size

  def append_element(self, val):
    new_node = self.__Node(val)
    self.__trailer.prev.next = new_node
    new_node.prev = self.__trailer.prev
    self.__trailer.prev = new_node
    new_node.next = self.__trailer
    self.__size += 1

  def insert_element_at(self, val, index):
    if self.__size == 0:
      pass
    elif self.__size <= index or index < 0:
      raise IndexError
    current = self.__header.next
    cur_index = 0
    while cur_index != index:
      current = current.next
      cur_index += 1
    new_node = self.__Node(val)
    current.prev.next = new_node
    new_node.prev = current.prev
    current.prev = new_node
    new_node.next = current
    self.__size += 1

  def remove_element_at(self, index):
    if self.__size <= index or index < 0:
      raise IndexError
    current = self.__header.next
    cur_index = 0
    while cur_index != index:
      current = current.next
      cur_index += 1
    current.prev.next = current.next
    current.next.prev = current.prev
    current.next = None
    current.prev = None
    self.__size -= 1
    return current.val

  def get_element_at(self, index):
    if self.__size <= index or index < 0:
      raise IndexError
    current = self.__header.next
    cur_index = 0
    while cur_index != index:
      current = current.next
      cur_index += 1
    return current.val

  def rotate_left(self):
    if self.__size == 0:
      return
    current = self.__header.next
    current.next.prev = self.__header
    self.__header.next = current.next
    self.__trailer.prev.next = current
    current.prev = self.__trailer.prev
    current.next = self.__trailer
    self.__trailer.prev = current
    
  def __str__(self):
    if self.__size == 0:
      return '[ ]'
    current = self.__header.next
    cur_index = 0
    result_str = '[ '
    while cur_index < self.__size - 1:
      result_str += str(current.val) + ', '
      current = current.next
      cur_index += 1
    result_str += str(current.val) + ' ]'
    return result_str

  def __iter__(self):
    self.current = self.__header
    return self

  def __next__(self):
    if self.current.next is self.__trailer:
      raise StopIteration
    self.current = self.current.next
    return self.current.val

if __name__ == '__main__':
  import random

  # creates three different types of lists

  def create_empty():
    return Linked_List()

  def create_one():
    one_ll = Linked_List()
    one_ll.append_element(random.randint(0,10000))
    return one_ll

  def create_many():
    many_ll = Linked_List()
    for i in range(0, 10):
      many_ll.append_element(random.randint(0,10000))
    return many_ll

  # manually create list to ensure the string representation is correct. ensures that
  # the string representation and method usage aren't messing up in a way that coincidentally
  # makes it seem they're working (not knowing the true values in lists with random values
  # this a possibility)
  manual_ll = Linked_List()
  manual_ll.append_element(5)
  manual_ll.append_element(3)
  manual_ll.append_element(6)
  manual_ll.append_element(4)
  manual_ll.insert_element_at(8, 2)
  manual_ll.remove_element_at(3)
  print('Expecting String: [ 5, 3, 8, 4 ]:')
  print(manual_ll)

  empty_ll = create_empty()
  one_ll = create_one()
  many_ll = create_many()

  # negative index in each linked list for each indexed method (should raise exception)
  print('Insert Element with Negative Indices (lists shouldn\'t change):\nEmpty Linked List:')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.insert_element_at(1, -1)
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.insert_element_at(1, -1)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.insert_element_at(1, -1)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')
  print('Remove Element with Negative Indices:\nEmpty Linked List:')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.remove_element_at(-1)
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.remove_element_at(-1)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.remove_element_at(-1)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')
  print('Get Element with Negative Indices:\nEmpty Linked List:')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.get_element_at(-1)
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.get_element_at(-1)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Node Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.get_element_at(-1)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')

  # new intact lists

  empty_ll = create_empty()
  one_ll = create_one()
  many_ll = create_many()

  # index too large for each linked list for each indexed method (should raise exception)
  # doesn't assume the list class passed the previous tests
  print('Insert Element with Indices Too Large:\nEmpty Linked List:')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.insert_element_at(1, 1)
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.insert_element_at(1, 1)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.insert_element_at(1, 9)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')
  print('Remove Element with Indices Too Large:\nEmpty Linked List:')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.remove_element_at(1)
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.remove_element_at(2)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.remove_element_at(10)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')
  print('Get Element with Indices Too Large:\nEmpty Linked List:')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.get_element_at(1)
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.get_element_at(2)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Node Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.get_element_at(10)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')
  
  # test all indexed methods on all three lists with valid indices

  # could make into a loop but ultimately it wouldn't make the code anymore readable because
  # there isn't an obvious loop possible

  print('Insert Element with Valid Indices:\nEmpty Linked List (Error Expected):')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.insert_element_at(1, 0)
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List (Error Expected):')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.insert_element_at(1, 0)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.insert_element_at(1, 8)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')

  empty_ll = create_empty()
  one_ll = create_one()
  many_ll = create_many()

  print('Remove Element with Valid Indices:\nEmpty Linked List (Error Expected):')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.remove_element_at(0) # error expected
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.remove_element_at(0)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.remove_element_at(9)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')

  # recreate empty just to make sure the it hasn't been modified by remove element before
  # testing it in get element
  empty_ll = create_empty()
  one_ll = create_one()
  many_ll = create_many()

  print('Get Element with Valid Indices:\nEmpty Linked List (Error Expected):')
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + '):')
  empty_ll.get_element_at(0) # error expected
  print(str(empty_ll) + ' (Size: ' + str(len(empty_ll)) + ')\n')
  print('One Node Linked List:')
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + '):')
  one_ll.get_element_at(0)
  print(str(one_ll) + ' (Size: ' + str(len(one_ll)) + ')\n')
  print('Ten Node Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.get_element_at(9)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')

  # recreate Many Nodes List
  many_ll = create_many()

  # test remove method on index 0, a middle index, and the last index
  print('Remove Index 0:\nTen Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.remove_element_at(0)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')

  # recreate many ll
  many_ll = create_many()

  # remove middle index on Many Nodes List
  print('Remove Index 5:\nMany Nodes Linked List:')
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + '):')
  many_ll.remove_element_at(5)
  print(str(many_ll) + ' (Size: ' + str(len(many_ll)) + ')\n')


  # test for loop (__iter__, __next__) and see if it matches what __str__ returns
  manual_ll = Linked_List()
  manual_ll.append_element(4)
  manual_ll.append_element(3)
  manual_ll.append_element(8)
  manual_ll.append_element(7)
  for i in manual_ll:
    print(i.val)
  print(manual_ll)

  # call size, test tail append, print, and call size to see if it changed
  many_ll = create_many()
  print('Size of 10 Nodes Linked List (should be 10): ' + str(len(many_ll)))
  many_ll.append_element(6)
  print('Size of 10 + 1 Nodes Linked List (should be 11): ' + str(len(many_ll)) + '\n')

  # recreate standard list set
  empty_ll = create_empty()
  one_ll = create_one()
  many_ll = create_many()

  # test the length method and see if it returns length (without sentinels)
  print('__len__ of an Empty List: ' + str(len(empty_ll)))
  print('__len__ of a One Node List: ' + str(len(one_ll)))
  print('__len__ of a Many Nodes List: ' + str(len(many_ll)))