# Code for prime numbers 
n=int(input())

count=0 
for i in range(2,n):
    if n%i==0:
        # print(n) 
        pass 
        # break
    else:
        # print('Yes it is a prime') 
        count+=1  


print(count) 

# Find the range of prime between given two numbers 

