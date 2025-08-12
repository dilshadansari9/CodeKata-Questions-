n1,n2=map(int, input().split())

# if n1>n2: 
#     while n2>0:
#         rem=n1%n2  
#         n1=n2 
#         n2=rem   
#     print(n1)
#     # if(rem==0):
#     #     print(n1)
# elif(n2>n1): 
# # if(n2>n1):
#     while n1>0:
#         rem=n2%n1 
#         n2=n1 
#         n1=rem 
#     print(n2)
#     # if(rem==0):
#     #     print(n2)
m=min(n1,n2)
for i in range(m,0,-1):
    if (n1%i==0) and (n2%i==0): 
        hcf=i
        break
print(hcf)        
