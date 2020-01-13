#accuracy, efficiency, clarity, communication
"""
You stumble across a random number generator on GitHub. The author believes that their
generator will create an infinite sequence of integers that won't repeat. Their random number
generator is seeded with a list of size N containing integers between 0 and N-1 (inclusive). It
then returns "random" numbers by iterating through the list. The generator starts by returning
the value at index 0. It then uses that value as the index for the next value to return, and
so on. If the generator was seeded with the list [1, 2, 0], the first number it would return would
be 1, then 2, then 0, and then it would repeat the sequence. Thus, the number of distinct
values would be 3.
"""

"""
Part a:
Write a function that takes as input the seed list of the random number generator of up to 1
million integers and returns the count of distinct integers the random number generator would
return. Your function may not modify the seed list. Hint: len(set(input_list)) does not produce
the right answer

Sample input: Sample output:
[1, 2, 0] 3
[4, 1, 3, 4, 2] 3



Some thoughts about the problem:
len(set(input_list)) doesn't work because not every index will be visited.
In example 2, we run into a cycle. We should be able to distinguish cycles
in the list
"""

def distinct_numbers(seed_list):
    """This function counts the number of distinct numbers returned by the random number generator

    Args:
        seed_list: the seed list of the random number generator up to 1 million integers
    Returns:
        distinct_count: the number of distinct numbers returned by the random number generator  
    """
    #catch if input has size zero or a size greater than 1000000 
    if len(seed_list) == 0:
        raise Exception("seed list is size 0")
    elif len(seed_list) > 1000000:
        raise Exception("use a seed list less than or equal to size 1000000")
    else:  
        number_list = [0]*len(seed_list) #distinct number list
        index = 0 #setting first index
        distinct_count = 0 #initializing distinct count
        while number_list[seed_list[index]] == 0: #used to detect cycles, if have a number in the number list we've already reached, it'll result in a cycle
            distinct_count = distinct_count + 1 #incrementing distinct count if value not found in number list
            number_list[seed_list[index]] = 1 # tracking in number list
            index = seed_list[index] #updating to next index
    return distinct_count

"""
Part b:
Can part a be done with O(1) auxiliary space (i.e. using only a constant amount of additional
memory)? If so, write a function that does it. If not, why not? Your function may not modify the
seed list.
"""

""" Part b answer: Yes, if i make the size of the number list 1000000 always, the function
    will use O(1) auxillary space    
"""
def distinct_numbers_O1(seed_list):
    """This function counts the number of distinct numbers returned by the random number generator

    Args:
        seed_list: the seed list of the random number generator up to 1 million integers
    Returns:
        distinct_count: the number of distinct numbers returned by the random number generator  
    """
    #catch if input has size zero or a size greater than 1000000 
    if len(seed_list) == 0:
        raise Exception("seed list is size 0")
    elif len(seed_list) > 1000000:
        raise Exception("use a seed list less than or equal to size 1000000")
    else:  
        number_list = [0]*1000000 #distinct number list
        index = 0 #first index
        distinct_count = 0
        while number_list[seed_list[index]] == 0:
            distinct_count = distinct_count + 1
            number_list[seed_list[index]] = 1
            index = seed_list[index]
    return distinct_count













 #initial try:
"""
 import copy
 def distinct_numbers(input_list):
    #copying input list and creating distinct number list
    seed_list = copy(input_list)
    number_list = [0]*len(seed_list)

    #first index
    index = seed_list[0]
    seed_list[0] = -1
    number_list[index] = 1
    distinct_count = 1
    
    while index != -1:
        past_index = index
        index = seed_list[index]
        seed_list[past_index] = -1
        if number_list[index] == 0:
            distinct_count = distinct_count + 1
            number_list[index] = 1

    return distinct_count
"""

