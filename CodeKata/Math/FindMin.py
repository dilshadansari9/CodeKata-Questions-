a=[9,5,1,5,3,-1,-2]
m=a[0]
for i in range(1,len(a)):
    if m>a[i]:
        m=a[i]

print(m)