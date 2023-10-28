# Problem : Given a binary array, sort it in linear time and constant space.
# The output should print all zeros, followed by all ones.


a = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
j = -1
for i in range(len(a)):
    if a[i] < 1:
        j = j+1  # Index increments only when the value is zero
        a[i], a[j] = a[j], a[i]  # associative swapping in python
print(a)

