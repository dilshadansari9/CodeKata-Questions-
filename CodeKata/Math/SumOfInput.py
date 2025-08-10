n=int(input())
total=0
# n1=int(n) 

while n!=0: 
    n1=n%10 
    total=total+n1 
    n=n//10 
print(total)  