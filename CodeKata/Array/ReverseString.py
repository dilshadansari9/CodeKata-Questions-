s=input("Enter string: ")

# i=-1
n=len(s)*(-1)

ans=[]
# while i>=n:
#     ans.append(s[i]) 
#     # print(ans)
#     i=i-1 
# print("".join(ans))


for i in range(-1,n-1,-1):  
    ans.append(s[i])
print("".join(ans))
