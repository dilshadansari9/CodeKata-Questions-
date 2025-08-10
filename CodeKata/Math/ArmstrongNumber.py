n=int(input("Enter a number: "))
sum=0
temp=n 
power=len(str(n))

while n!=0:
    rem=n%10 
    cub=rem**power 
    sum=sum+cub 
    n=n//10
if temp==sum:
    print('true')
else:
    print('false')