a=['A23' ,'B56' ,'B56', 'C79' ,'D16']
s=[]
print(type(s))
for i in a:
    if i not in s:
        s.append(i)

print(s) 