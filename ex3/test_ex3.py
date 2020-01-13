from ex3 import csv_missing_integer_finder_parts_ab, csv_missing_integer_finder
import unittest
import numpy as np
import random
import csv

class test_missing_integer_finder(unittest.TestCase):
    
    def test_result_part_ab(self):
        """
        A = [value for value in range(1,1000001)]
        B = [value for value in range(1,1000001)]
        A.remove(10)
        B.remove(10)
        A.remove(9176)
        #10 from both, 9176 from A
        random.shuffle(A)
        random.shuffle(B)
        with open('foo.csv', 'w', newline='') as csvfile:
            fieldnames = ['A', 'B']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i, j in zip(A, B):
                writer.writerow({'A': i, 'B': j})
        #had to add one missing value in column B
        """
        [calculated_result_a, calculated_result_ab] = csv_missing_integer_finder_parts_ab('foo.csv')
        assert calculated_result_a == 9176
        assert calculated_result_ab == 10
    
    def test_result_part_c(self):
        [calculated_result_a, calculated_result_ab] = csv_missing_integer_finder('foo.csv', 1000000)
        assert calculated_result_a == 9176
        assert calculated_result_ab == 10