n=int(input("Enter size of array: "))

ids=list(map(int,input().split()))

for i in range(n):
    for j in ids:
        if ids[i]==j:
            ans=ids[j]  
            print(ans) 
            break 
        
# THis code is incorrect. We will write for this after one week 

