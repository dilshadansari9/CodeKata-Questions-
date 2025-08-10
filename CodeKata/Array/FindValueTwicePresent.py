# n=int(input("Enter the size of the array: "))

li=[13,12,13,12,13]
l=li 
iterator=0 
count=0  
for i in li:
    if (l[iterator]==i):
        count=count+1 
        value=i  
if count==2:
    print(value) 


