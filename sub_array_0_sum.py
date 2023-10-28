# We should check if array has all positive or all negative elements | Not help
# Maybe sorting all the elements would help. It would help in 2 pointer logic
# Go in order need no re-arrange elements!
# No Question will be asked if sum = 0 without negative and positive elements
main_array = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

for n in range(2, len(main_array)+2):

    for items in range(len(main_array)-n+1):
        new_list = []
        new_list = main_array[items:items+n]
        output = sum(new_list)
        if output == 0:
            print(new_list)
