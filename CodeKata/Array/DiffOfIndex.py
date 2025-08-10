a=[1,6,4,0,3]
large=a[0]
small=a[0]
i1=0
j=0 
for i in range(1,len(a)):
    if large<a[i]:
        large=a[i]
        i1=i 
    if small>a[i]:
        small=a[i]
        j=i 


print(large)
print(i1)
print(small)
print(j) 
print(i1-j) 