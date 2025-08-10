n=int(input())

even=[]
odd=[]

while n!=0:
    rem=n%10 
    if(rem%2==0):
        even.append(str(rem)) 
        # print(" ".join(even)) 
    else:
        odd.append(str(rem))
        # print(" ".join(odd))
    n=n//10 
even.reverse()
odd.reverse()
print(" ".join(even)) 
print(" ".join(odd)) 
