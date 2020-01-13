from ex1 import distinct_numbers, distinct_numbers_O1
import unittest
import numpy as np
import random

class test_flatten_list(unittest.TestCase):
    
    def test_finalresult1_distinct_numbers(self):
        input_list = [1,2,0]
        calculated_result = distinct_numbers(input_list)
        assert calculated_result == 3
    
    def test_finalresult2_distinct_numbers(self):
        input_list = [4, 1, 3, 4, 2]
        calculated_result = distinct_numbers(input_list)
        assert calculated_result ==3
    
    def test_input_list_not_modified(self):
        input_list = [5, 3, 1, 4, 0, 1]
        calculated_result = distinct_numbers(input_list)
        assert np.all(input_list == [5, 3, 1, 4, 0, 1])
    
    def test_input_list_zero(self):
        input_list = [0]
        calculated_result = distinct_numbers(input_list)
        assert calculated_result == 1

    def test_1mil_input(self):
        input_list = [random.randint(0, 1000000) for i in range(1000000)]
        calculated_result = distinct_numbers(input_list)
        print(calculated_result)
        assert len(input_list) == 1000000
    
    def test_zero_size_input_list(self):
        self.assertRaises(Exception, distinct_numbers, [])
    
    def test_greater_1mil_size_input_list(self):
        input_list = [random.randint(0, 1000000) for i in range(1000001)]
        self.assertRaises(Exception, distinct_numbers, input_list)
    
    def test_finalresult1_distinct_numbers_O1(self):
        input_list = [1,2,0]
        calculated_result = distinct_numbers_O1(input_list)
        assert calculated_result == 3
    
    def test_finalresult2_distinct_numbers_O1(self):
        input_list = [4, 1, 3, 4, 2]
        calculated_result = distinct_numbers_O1(input_list)
        assert calculated_result ==3
    
    def test_input_list_not_modified_O1(self):
        input_list = [5, 3, 1, 4, 0, 1]
        calculated_result = distinct_numbers_O1(input_list)
        assert np.all(input_list == [5, 3, 1, 4, 0, 1])
    
    def test_input_list_zero_O1(self):
        input_list = [0]
        calculated_result = distinct_numbers_O1(input_list)
        assert calculated_result == 1

    def test_1mil_input_O1(self):
        input_list = [random.randint(0, 1000000) for i in range(1000000)]
        calculated_result = distinct_numbers_O1(input_list)
        print(calculated_result)
        assert len(input_list) == 1000000
    
    def test_zero_size_input_list_O1(self):
        self.assertRaises(Exception, distinct_numbers_O1, [])
    
    def test_greater_1mil_size_input_list_O1(self):
        input_list = [random.randint(0, 1000000) for i in range(1000001)]
        self.assertRaises(Exception, distinct_numbers_O1, input_list)


    