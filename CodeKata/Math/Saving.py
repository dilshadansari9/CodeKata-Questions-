n=int(input())

m0=1000
m1=1000

total=m1+m0 


for i in range(n):
        next_month=m1+m0 
        m0=m1  
        m1=next_month 
        total+=next_month 
        # print(total)

print(total)