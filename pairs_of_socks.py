# In a given list of arrays we need to find the 
# pairs of numbers and list them. To do this, we could use a counter 
# Identify if the counter values when divided by 2 gives us 0 in reminder 

# Input 1st line has the number of values 
# Where ease  input 2 has the list 

# Implementation of counter in the best way 

# Pseudo code 

# Use a counter to identify the pairs of socks. I am using the generator expression snippet 


# The counter function played an important role by counting the elements in the array 

def counter_function(sample_list):
    
    counter_elements = ((elements, sum(1 for e in sample_list if e == elements)) for elements in set(sample_list))
    return dict(counter_elements)

# This part of the code is simple. 

def finding_pairs_of_socks(sample_list):
    
    counted_elements = counter_function(sample_list)
    pair_counter = 0
    
    for keys, values in counted_elements.items():
        if (counted_elements[keys] % 2 == 0):
            pair_counter += int(counted_elements[keys] / 2)
        else:
            paired_values = (counted_elements[keys] - 1)
            pair_counter += int(paired_values / 2)
            
    return pair_counter        

sample_list = [10, 20, 20, 10, 10, 30, 50, 10, 20]
output = finding_pairs_of_socks(sample_list)
print(output)