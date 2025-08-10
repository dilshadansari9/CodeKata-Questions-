n, w = map(int, input().split())
arr = list(map(int, input().split()))
a = []

for i in range(n - w + 1):
    found = False
    for j in range(w):
        if arr[i + j] == 0:
            a.append(str(i + j + 1))  # 1-based index
            found = True
            break
    if not found:
        a.append(str(-1))

print(" ".join(a)) 
