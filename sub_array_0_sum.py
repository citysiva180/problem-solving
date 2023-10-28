# We should check if array has all positive or all negative elements | Not help
# Maybe sorting all the elements would help. It would help in 2 pointer logic
# Go in order need no re-arrange elements!
# No Question will be asked if sum = 0 without negative and positive elements

main_array = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

for n in range(2, len(main_array)+1):
    for items in range(len(main_array)-n+1):
        new_list = []
        new_list = main_array[items:items+n]
        output = sum(new_list)
        if output == 0:
            print(new_list)

# Notes :

# 1. Remember that when you iterate using range or even using slice, if you say array[0:10]
# it will take only 9 elements! 0,1,2,3,4,5,6,7,8,9

# 2. The Main for loop is the loop that determines number elements for the sub-array list
# 3. new_list = main_array[items:items+n] | will give you main_array[0:0+n] wherease this n
# dependent on main loop!
