Coding Challenges

Challenge 1 Information


Challenge Prompt:

You stumble across a random number generator on GitHub. Their random number
generator is seeded with a list of size N containing integers between 0 and N-1 (inclusive). It
then returns "random" numbers by iterating through the list. The generator starts by returning
the value at index 0. It then uses that value as the index for the next value to return, and
so on. If the generator was seeded with the list [1, 2, 0], the first number it would return would
be 1, then 2, then 0, and then it would repeat the sequence. Thus, the number of distinct
values would be 3.

Write a function that takes as input the seed list of the random number generator of up to 1
million integers and returns the count of distinct integers the random number generator would
return. Your function may not modify the seed list and must use constant auxilary space.


Solution Explanation:

The goal of challenge 1 is to count the distinct integers from the random number generator. At first the solution may seem trivial, perhaps as easy as len(set(seed_list)). The solution is less trivial however when you consider the potential for cycles in seed_list.
 
Here’s an example of a seed_list with a cycle:
	Seed_list = [4, 0, 3, 4, 2]
The random number generator will produce a sequence containing 4, 2, and 0. The 3 digits will repeat continuously because the last number, 0, points to the zeroth index which produces 4 again. 
An effective solution will include cycle detection.

Walkthrough of Solution:

The solution detects cycles via a visited numbers list called “numbers_list” (initialized on line 46). The initial index and count of distinct numbers are initialized on lines 47 and 48 respectively. The while block from lines 49-52 continues as long as no cycle is detected. During each loop, the count of distinct numbers is incremented (line 50), the visited numbers list is marked (line 51), and the index is updated to the next index in the seed_list (line 52). If the value in the next index in the seed list has not been visited according to the visited number_list, the loop repeats. Finally, the function returns the count of distinct numbers.




