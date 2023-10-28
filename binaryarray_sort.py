a = [0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1]
j=-1
for i in range(len(a)):
    if a[i]< 1:
        j = j+1
        a[i],a[j] = a[j],a[i]
print(a)