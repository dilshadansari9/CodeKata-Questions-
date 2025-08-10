a='mississipie'
ans=[]
for i in a:

    if a.count(i) >1:
        continue
    else:
        ans.append(i)
print(ans) 
print("".join(ans))
