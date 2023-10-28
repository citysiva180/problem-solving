# in this section we would be building re-usable code snippets for the following 
# 1. Counting occurences 
# 2. Counting Duplicates 
# 3. Removing Duplicates 
# 4. Removing Duplicates based on a count 
# 5. Finding Non Duplicates 
# 6. Pairs of Numbers whose sum = N
# 7. Practice on Mutability - Explanation 
# 8. Sum of arrays, dictionaries, list and tuples 
# 9. Anagram 
# 10. Palindrome 
# 11. Perform, sum, multiply, add and divide on individual list of elements 
# 12. Using Logical gates in python
# 13. Finding Permutations and Combinations in python | use Itertools and Collections Module!


 #==========================================
# First Approach 

def count_elements_generator(iterable):
    return ((element, sum(1 for e in iterable if e == element)) for element in set(iterable))

# Example usage:
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result_generator = count_elements_generator(my_list)
for element, count in result_generator:
    print(f'{element}: {count}')

#=============================================
# Second Approach 

def count_elements(iterable):
    # Initialize an empty dictionary to store the counts
    counts = {}
    
    # Use a dictionary comprehension to count the elements in the iterable
    for element in iterable:
        counts[element] = counts.get(element, 0) + 1
    
    return counts

# Example usage:
my_list = [1,1,1,1,1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_elements(my_list)
print(result)

#=============================================
