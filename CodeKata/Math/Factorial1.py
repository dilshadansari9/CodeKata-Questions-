n=int(input("Enter a number: "))
fact=1
if n<=1:
    print(1)
else:
    for i in range(2,n+1):
        fact=fact*i 
    print(fact)