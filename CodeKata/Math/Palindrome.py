n=int(input())
num=0
n1=n 
while n!=0:
    digit=n%10 
    num=num*10+digit 
    n=n//10 
print(num)
if num==n1: 
    print('true')
else:
    print('false')