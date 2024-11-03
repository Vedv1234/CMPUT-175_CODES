"""
Author: Ved Vyas
Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
Functionality of code: This is my test suite for the selection sort implementation. Similar to my 
merge sort tests, I've created a comprehensive set of test cases to verify that my selection sort 
works correctly. What's interesting here is that I need to pass the length of the array as a 
parameter, which is different from my merge sort tests.
"""

# I'm following the unittest documentation from Python's official docs
import unittest
from exercise_1 import *
import random

class TestEx1(unittest.TestCase):
    """My test class for checking the selection sort implementation"""
    
    def test_empty_array(self):
        """I'm testing how my sort handles an empty array"""
        input_array = []
        recursive_selection_sort(input_array, 0)
        self.assertEqual(input_array, [])
        
    def test_one_element(self):
        """I'm testing how my sort handles a single-element array"""
        input_array = [0]
        recursive_selection_sort(input_array, 1)
        self.assertEqual(input_array, [0])
        
    def test_in_and_out_of_order(self):
        """I'm testing both already sorted and unsorted arrays"""
        # First, I test with numbers out of order
        input_array = [3,2,1]
        recursive_selection_sort(input_array, 3)
        self.assertEqual(input_array, [3,2,1])
        
        # Then I test with numbers in ascending order
        input_array = [1,2,3]
        recursive_selection_sort(input_array, 3)
        self.assertEqual(input_array, [3,2,1])
        
    def test_repeated_elements(self):
        """I'm testing how my sort handles duplicate numbers"""
        input_array = [3,1,1,5]
        recursive_selection_sort(input_array, 4)
        self.assertEqual(input_array, [5,3,1,1])
        
    def test_mixed_numbers(self):
        """I'm testing with a mix of positive, negative, and zero values"""
        input_array = [2,-5,0,3,-2,4]
        recursive_selection_sort(input_array, 6)
        self.assertEqual(input_array, [4,3,2,0,-2,-5])
        
    def test_random_numbers(self):
        """I'm testing with a large array of random numbers"""
        input_array = [random.randint(1,1000) for i in range(500)]
        sorted_list = sorted(input_array, reverse=True)
        recursive_selection_sort(input_array, 500)
        self.assertEqual(input_array, sorted_list)

if __name__ == "__main__":
    # I'm running all my tests
    unittest.main()