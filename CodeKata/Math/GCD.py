li=[1,2,3,4,5]
i=1 
while i>0:
    if all(i%j ==0 for j in li):
        print(i)
        break 
    i+=1 
    


 