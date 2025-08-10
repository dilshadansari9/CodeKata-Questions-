n=int(input())

ans=[]
while n!=0:
    rem=n%10 
    ans.append(str(rem))
    n=n//10 
ans.reverse()
print(" ".join(ans)) 