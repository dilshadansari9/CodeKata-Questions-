n=int(input("Enter number to reverse: "))

ans=0 

while n!=0:
    rem=n%10 
    ans=ans*10+rem 
    n=n//10 
print(ans)