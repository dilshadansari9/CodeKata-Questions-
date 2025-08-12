a=[4,2,1,2,3]

ans=[]

# This is my approach 
# for i in range(1,len(a),2):  
#     temp=a[i]
#     temp2=a[i-1]
#     ans.append(temp)  
#     ans.append(temp2) 
# if len(a)%2!=0:
#     ans.append(a[len(a)-1])

for i in range(1, len(a), 2):
    a[i], a[i-1] = a[i-1], a[i]

print(a)
# print(ans)  