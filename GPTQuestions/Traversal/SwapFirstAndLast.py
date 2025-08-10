arr = [1, 2, 3, 4, 5]
# Output: [5, 2, 3, 4, 1]
num=arr[0]
arr[0]=arr[-1]
arr[-1]=num 

print(arr)