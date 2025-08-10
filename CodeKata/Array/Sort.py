a=[4,1,6,3,6,7,8]
min=a[0]
s=[]
for i in range(len(a)):
    for j in range(1,len(a)):
        if min>a[j]:
            min=a[j]      
            a[j]=a[i] 
            s.append(min) 
        else:
    
             s.append(min)
print(s) 
            
