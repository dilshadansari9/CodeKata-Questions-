a=[1, -2, -3, -4, 5 ,6, -7]

# a=[1,2,3,4,5]

n=len(a)
k=3 
s=[]

for i in range(n-k+1):
    found=False  
    for j in range(i,i+k):
        if a[j]<0:
            s.append(a[j])
            found=True 
            break
    if not found:
        s.append(0)

    
print(s) 