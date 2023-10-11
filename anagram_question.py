#  Given two strings,  and , that may or may not be of the same length, 
# determine the minimum number of character deletions required to make  
# and  anagrams. Any characters can be deleted from either of the strings   

# Re-Usable Counter
def counter(string_x):
    freq = {}
    for c in set(string_x):
        freq[c] = string_x.count(c)
    return freq


def makeAnagram(a, b):
    
    first = counter(a)
    second = counter(b)
    
    # logical operators to find common and uncommon keys 
    uncommon_keys = first.keys() ^ second.keys() 
    common_keys = first.keys() & second.keys()

    new_dict = {}
    for items in list(uncommon_keys):
        if items in first.keys():
            new_dict[items] = first[items]
        if items in second.keys():
            new_dict[items] = second[items]

    uncommon_sum = sum(new_dict.values())

    common_sum = 0
    for keys in list(common_keys):
        diff = abs(second[keys] - first[keys])
        if diff != 0:
            common_sum += diff

    final = uncommon_sum + common_sum
    return final    

makeAnagram("cdf","dec")