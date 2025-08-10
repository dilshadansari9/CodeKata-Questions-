arr = [0, 3, 0, 5, 0, 7]
# Output: [3, 5, 7]
a=[]
for i in arr:
    if i==0:
        continue
    else:
        a.append(i)

print(a)