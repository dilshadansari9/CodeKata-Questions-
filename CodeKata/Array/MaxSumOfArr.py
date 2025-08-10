arr = [2, 6, 5, 1, 3, 2]
k=2
n=len(arr) 
max_sum=float('-inf')

for i in range(n-k+1):
    sum=0
    for j in range(i,i+k):
        sum=sum+arr[j]  
    max_sum=max(max_sum,sum) 
print(max_sum) 