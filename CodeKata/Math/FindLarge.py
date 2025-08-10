a=[8,2,9,4,5,26,7,1,9]

m=a[0]
for i in range(1,len(a)):
    if m<a[i]:
        m=a[i]
print(m) 