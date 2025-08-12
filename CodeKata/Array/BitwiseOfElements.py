a=[4,3,2,1]

ans=a[0]
for i in range(len(a)): 
    ans=ans & a[i]
print(ans)  
