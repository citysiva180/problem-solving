# Finding Pairs in a list which make up to a given sum 
# For this we need an iterator or an enumerator 
# Or Pair all the numbers and sum them??? 
# Will sorting the array help in any case?
# Odd vs Even 
from itertools import combinations 
def sum_of_pairs(sample_list, target_sum):

    pairs = []
    for pair in combinations(sample_list, 2):
        if sum(pair) == target_sum:
            pairs.append(pair)
    return pairs
        
sample_list = [8, 7, 2, 5, 3, 1]
target = 10 
output =  sum_of_pairs(sample_list,target)
print(output)

