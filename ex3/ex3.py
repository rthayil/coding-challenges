"""
Write a program that reads in a CSV file with two columns, “A” and “B”. Column “A” contains
999,998 strings representing unique integers from 1 to 1,000,000 (2 integers are missing).
Column “B” contains 999,999 strings representing unique integers from 1 to 1,000,000 (1
integer is missing), and the missing integer is the same as one of the missing integers
in Column “A”.

Part a:
Your program should print the integer that exists in column “B”, but not in column “A”.

Part b:
Your program should also print out the integer that’s missing from both columns.

Part c:
Can part b be done with less than O(n) auxiliary space (i.e. if the length of the CSV doubled, your
memory usage would not double) and O(n) time complexity? If so, write a program that does it.
If not, why not?
"""

import csv
import numpy as np

def csv_missing_integer_finder_parts_ab(filename):
    """ This function returns the common missing integer in columns A and B and the integer
        missing in only column A

    Args:
        filename: the csv containing the columns a and b.
    Returns:
        missing_a_only: part a response, value thats missing in only column a
        missing_ab: part b response, value thats missing in both columns 
    """
    missing = [0]*1000001 #list to keep track of numbers that are in the list
    with open(str(filename), 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader: 
            if row[0]: 
                missing[int(row[0])] = missing[int(row[0])] + 1 #if number is in col A, add 1
            if row[1]:
                missing[int(row[1])] = missing[int(row[1])] + 1 #if number is in col B, add 1
    
    for i, value in enumerate(missing):
        if value != 2: #if number is in col A and B, missing list index will have value of 2
            if value == 1:
                missing_a_only = i
            elif value == 0:
                missing_ab = i

    return missing_a_only, missing_ab


#part c, since all integers are unique from 1 to 1mil, can use sum to store info
def csv_missing_integer_finder(filename, range_value):
    """ This function returns the common missing integer in columns A and B and the integer
        missing in only column A

    Args:
        filename: the csv containing the columns a and b.
        range_value: highest value of lists. In parts a and b, this was 1000000
    Returns:
        missing_a_only: part a response, value thats missing in only column a
        missing_ab: part b response, value thats missing in both columns 
    """
    
    mil_sum = np.sum([value for value in range(1,range_value+1)]) #calculating each time in case value can be variable, would keep constant if always 1mil
    a_sum = 0 #will store sum of all values of a
    b_sum = 0 #will store sum of all values of b
    with open(str(filename), 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            if row[0]: 
                a_sum = int(row[0]) + a_sum #adding sum while reading from csv so won't need to store in array
            if row[1]:
                b_sum = int(row[1]) + b_sum
    missing_ab = mil_sum-b_sum #finding missing value in b column
    missing_a_only = mil_sum-a_sum-missing_ab #finding value thats missing only in a column

    return missing_a_only, missing_ab

