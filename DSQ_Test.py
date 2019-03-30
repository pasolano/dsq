import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # Deque Tests

  # Empty List Test

  def test_empty_deque(self):
    self.assertEqual('[ ]', str(self.__deque))

  # Length Tests

  def test_length_no_entry_deque(self):
    self.assertEqual(0, len(self.__deque))

  def test_length_one_entry_deque(self):
    self.__deque.push_back('Data')
    self.assertEqual(1, len(self.__deque))

  def test_length_three_entry_deque(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_back('Rocks')
    self.assertEqual(3, len(self.__deque))

  # Push Front Tests

  def test_push_front_one_entry_deque(self):
    self.__deque.push_front('Data')
    self.assertEqual('[ Data ]', str(self.__deque))

  def test_push_front_three_entry_deque(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__deque))

  # Pop Front Tests

  def test_pop_front_no_entry_deque(self):
    returned = self.__deque.pop_front()
    self.assertEqual(None, returned)

  def test_pop_front_no_entry_not_modified_deque(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_one_entry_deque(self):
    self.__deque.push_front('Data')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_one_entry_deque_returned_value(self):
    self.__deque.push_front('Data')
    returned = self.__deque.pop_front()
    self.assertEqual('Data', returned)

  def test_pop_front_three_entry_deque(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.pop_front()
    self.assertEqual('[ Structures, Rocks ]', str(self.__deque))
  
  def test_pop_front_three_entry_deque_returned_value(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    returned = self.__deque.pop_front()
    self.assertEqual('Data', returned)

  def test_pop_two_front_three_entry_deque(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('[ Rocks ]', str(self.__deque))

  def test_pop_two_front_three_entry_deque_first_returned_value(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    returned = self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('Data', returned)

  def test_pop_two_front_three_entry_deque_second_returned_value(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.pop_front()
    returned = self.__deque.pop_front()
    self.assertEqual('Structures', returned)

  # Peek Front Tests

  def test_peek_front_no_entry_deque(self):
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)

  def test_peek_front_one_entry_deque(self):
    self.__deque.push_front('Data')
    returned = self.__deque.peek_front()
    self.assertEqual('Data', returned)

  def test_peek_front_three_entry_deque(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    returned = self.__deque.peek_front()
    self.assertEqual('Data', returned)

  def test_peek_front_not_modified_deque(self):
    self.__deque.push_front('Data')
    self.__deque.peek_front()
    self.assertEqual('[ Data ]', str(self.__deque))

  # Push Back Tests

  def test_push_back_one_entry_deque(self):
    self.__deque.push_back('Data')
    self.assertEqual('[ Data ]', str(self.__deque))

  def test_push_back_three_entry_deque(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_back('Rocks')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__deque))

  # Pop Back Tests

  def test_pop_back_no_entry_deque(self):
    returned = self.__deque.pop_back()
    self.assertEqual(None, returned)

  def test_pop_back_no_entry_deque_not_modified(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_one_entry_deque(self):
    self.__deque.push_front('Data')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_one_entry_deque_return_value(self):
    self.__deque.push_front('Data')
    returned = self.__deque.pop_back()
    self.assertEqual('Data', returned)

  def test_pop_back_three_entry_deque(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.pop_back()
    self.assertEqual('[ Data, Structures ]', str(self.__deque))

  def test_pop_back_three_entry_deque_return_value(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    returned = self.__deque.pop_back()
    self.assertEqual('Rocks', returned)

  def test_pop_two_back_three_entry_deque(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.assertEqual('[ Data ]', str(self.__deque))

  def test_pop_two_back_three_entry_deque_first_returned_value(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    returned = self.__deque.pop_back()
    self.__deque.pop_back()
    self.assertEqual('Rocks', returned)

  def test_pop_two_back_three_entry_deque_second_returned_value(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.pop_back()
    returned = self.__deque.pop_back()
    self.assertEqual('Structures', returned)

  # Peek Back Tests

  def test_peek_back_no_entry_deque(self):
    returned = self.__deque.peek_back()
    self.assertEqual(None, returned)

  def test_peek_back_one_entry_deque(self):
    self.__deque.push_front('Data')
    returned = self.__deque.peek_back()
    self.assertEqual('Data', returned)

  def test_peek_back_three_entry_deque(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    returned = self.__deque.peek_back()
    self.assertEqual('Rocks', returned)

  def test_peek_back_not_modified_deque(self):
    self.__deque.push_front('Data')
    self.__deque.peek_back()
    self.assertEqual('[ Data ]', str(self.__deque))

  # Stack Tests

  # Empty List Test

  def test_empty_stack(self):
    self.assertEqual('[ ]', str(self.__stack))

  # Length Tests

  def test_length_no_entry_stack(self):
    self.assertEqual(0, len(self.__stack))

  def test_length_one_entry_stack(self):
    self.__stack.push('Data')
    self.assertEqual(1, len(self.__stack))

  def test_length_three_entry_stack(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.__stack.push('Rocks')
    self.assertEqual(3, len(self.__stack))

  # Push Tests

  def test_push_one_entry_stack(self):
    self.__stack.push('Data')
    self.assertEqual('[ Data ]', str(self.__stack))

  def test_push_three_entry_stack(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__stack))

  # Pop Tests

  def test_pop_no_entry_stack(self):
    returned = self.__stack.pop()
    self.assertEqual(None, returned)

  def test_pop_no_entry_stack_not_modified(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_one_entry_stack(self):
    self.__stack.push('Data')
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_one_entry_stack_returned_value(self):
    self.__stack.push('Data')
    returned = self.__stack.pop()
    self.assertEqual('Data', returned)

  def test_pop_three_entry_stack(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.__stack.pop()
    self.assertEqual('[ Structures, Rocks ]', str(self.__stack))

  def test_pop_two_entry_stack_returned_value(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    returned = self.__stack.pop()
    self.assertEqual('Data', returned)

  def test_pop_two_three_entry_stack(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ Rocks ]', str(self.__stack))

  def test_pop_two_three_entry_stack_first_returned_value(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    returned = self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('Data', returned)

  def test_pop_two_three_entry_stack_second_returned_value(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.__stack.pop()
    returned = self.__stack.pop()
    self.assertEqual('Structures', returned)

  # Peek Tests

  def test_peek_no_entry_stack(self):
    returned = self.__stack.peek()
    self.assertEqual(None, returned)

  def test_peek_one_entry_stack(self):
    self.__stack.push('Data')
    returned = self.__stack.peek()
    self.assertEqual('Data', returned)

  def test_peek_three_entry_stack(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    returned = self.__stack.peek()
    self.assertEqual('Data', returned)

  def test_peek_not_modified_stack(self):
    self.__stack.push('Data')
    self.__stack.peek()
    self.assertEqual('[ Data ]', str(self.__stack))

  # Queue Tests

  # Empty List Test

  def test_empty_queue(self):
    self.assertEqual('[ ]', str(self.__queue))

  # Length Tests

  def test_length_no_entry_queue(self):
    self.assertEqual(0, len(self.__queue))

  def test_length_one_entry_queue(self):
    self.__queue.enqueue('Data')
    self.assertEqual(1, len(self.__queue))

  def test_length_three_entry_queue(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    self.assertEqual(3, len(self.__queue))

  # Enqueue Tests

  def test_enqueue_one_entry_queue(self):
    self.__queue.enqueue('Data')
    self.assertEqual('[ Data ]', str(self.__queue))

  def test_enqueue_three_entry_queue(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__queue))

  # Dequeue Tests

  def test_dequeue_no_entry_queue(self):
    returned = self.__queue.dequeue()
    self.assertEqual(None, returned)

  def test_dequeue_no_entry_queue_not_modified(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_one_entry_queue(self):
    self.__queue.enqueue('Data')
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_one_entry_queue_returned_value(self):
    self.__queue.enqueue('Data')
    returned = self.__queue.dequeue()
    self.assertEqual('Data', returned)

  def test_dequeue_three_entry_queue(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    self.__queue.dequeue()
    self.assertEqual('[ Structures, Rocks ]', str(self.__queue))

  def test_dequeue_three_entry_queue_returned_value(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    returned = self.__queue.dequeue()
    self.assertEqual('Data', returned)

  def test_dequeue_two_three_entry_queue(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ Rocks ]', str(self.__queue))

  def test_dequeue_two_three_entry_queue_first_returned_value(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    returned = self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('Data', returned)

  def test_dequeue_two_three_entry_queue_second_returned_value(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    self.__queue.dequeue()
    returned = self.__queue.dequeue()
    self.assertEqual('Structures', returned)

if __name__ == '__main__':
  unittest.main()