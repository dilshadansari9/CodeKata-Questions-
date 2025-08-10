n1=int(input())

fact=1
for i in range(1,n1):
    # print("fact*i",fact*i)
    fact=fact*i +fact 

     
    # print(fact)

print(fact)