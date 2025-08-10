a=[1,1,1,1,1]
sum=0 
a1=[]
for i in a:
    
    sum=sum+i 
    if sum%2==0:
        a1.append(sum)
    else:
        a1.append(i) 

print(a1) 