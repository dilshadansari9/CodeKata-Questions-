arr = [2, -3, 5, -1, 0,-2,2,-5]
# Output: [2, 0, 5, 0, 0]

for i in range(len(arr)):
    if arr[i]<0:
        arr[i]=0 
print(arr)