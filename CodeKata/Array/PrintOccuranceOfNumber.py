a=[1 ,1, 1, 2, 2, 2, 3, 8, 9, 7]

a2=[1 ,2 ,3 ,0 ,5]
total=[] 
count=0 
for i in a2:
    # found=False 
    for j in a:
        if i==j:
            count+=1 
            # found=True 
    if count==0:
        total.append('n')
    else:
        total.append(count)  
    count=0  
print(total) 
