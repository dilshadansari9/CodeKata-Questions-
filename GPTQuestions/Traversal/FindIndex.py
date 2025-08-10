arr = [5, 8, 2, 10]
target = 11
# Output: 2 (index of target)

for i in range(len(arr)):
    if target==arr[i]:
        print(i)
        break
    else:
        print(-1)
        break