a=[1,4,2]
a.sort()
b=[6,3,5]
b.sort(reverse=True)
total=a+b 
print(total) 
# ans=len(total)
# ans.append(a+b)
# print(ans) 
ans=[]
for i in total:
    # print(i)
    ans.append(str(i))

print(" ".join(ans))