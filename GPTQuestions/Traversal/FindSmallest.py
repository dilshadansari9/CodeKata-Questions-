arr = [3, 1, 6, 0, 9, -1]
# Output: 0
small=arr[0]
for i  in range(len(arr)):
    if small>arr[i]:
        small=arr[i]

print(small)