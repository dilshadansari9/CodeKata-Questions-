n=int(input("Enter a number: "))
li=[]

for i in range(1,n+1): 
    if i%2==0:
        li.append(str(i))

print(" ".join(li)) 