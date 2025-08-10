arr = [1, 2, 3, 4]
# Output: [4, 3, 2, 1]

n=len(arr)-1 
r=[]
# while n>=0:
#     r.append(arr[n])
#     n-=1 
# print(r)

for i in range(n,-1,-1):
    r.append(arr[i]) 

print(r)