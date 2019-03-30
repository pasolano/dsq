from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__entries = 0
    self.__head = 0
    self.__tail = 0
    
  def __str__(self):
    result_str = '[ '
    current = self.__head
    while current != self.__tail:
      if self.__contents[current] == None:
        pass
      else:
        result_str += str(self.__contents[current]) + ', '
      current += 1
      if current == self.__capacity:
        current = 0
    if self.__contents[self.__tail] == None:
      return '[ ]'
    result_str += str(self.__contents[self.__tail]) + ' ]'
    return result_str
    
  def __len__(self):
    return self.__entries

  def __grow(self):
    if self.__entries == self.__capacity:
      new_contents = [None] * (2 * self.__capacity)
      old_index = self.__head
      new_index = 0
      head_val = self.__head
      tail_val = self.__tail
      while new_index != self.__capacity:
        if old_index == self.__capacity:
          old_index = 0
        new_contents[new_index] = self.__contents[old_index]
        if old_index == head_val:
          self.__head = new_index
        elif old_index == tail_val:
          self.__tail = new_index
        old_index += 1
        new_index += 1
      self.__contents = new_contents
      self.__capacity = self.__capacity * 2
    else:
      pass
    
  def push_front(self, val):
    self.__grow()
    if self.__head == 0:
      self.__head = self.__capacity - 1
      self.__contents[self.__capacity - 1] = val
    else:
      self.__head -= 1
      self.__contents[self.__head] = val
    self.__entries += 1
    
  def pop_front(self):
    try:
      pop_val = self.__contents[self.__head]
      self.__contents[self.__head] = None
      if self.__head == self.__capacity - 1:
        self.__head = 0
      else:
        self.__head += 1
      self.__entries -= 1
      return pop_val
    except IndexError:
      return None
    
  def peek_front(self):
    try:
      return self.__contents[self.__head]
    except IndexError:
      return None
    
  def push_back(self, val):
    self.__grow()
    if self.__tail == self.__capacity - 1:
      self.__tail = 0
      self.__contents[0] = val
    else:
      self.__tail += 1
      self.__contents[self.__tail] = val
    self.__entries += 1

  def pop_back(self):
    try:
      pop_val = self.__contents[self.__tail]
      self.__contents[self.__tail] = None
      if self.__tail == 0:
        self.__tail = self.__capacity - 1
      else:
        self.__tail -= 1
      self.__entries -= 1
      return pop_val
    except IndexError:
      return None

  def peek_back(self):
    try:
      return self.__contents[self.__tail]
    except IndexError:
      return None

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass