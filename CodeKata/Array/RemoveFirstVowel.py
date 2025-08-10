s="education"
ans=''
i=0 
low=['a','e','i','o','u']
cap=['A','E','I','O','U']

while i<len(s):
    if s[i] in low or s[i] in cap:
        ans=s[:i] + s[i+1:] 
        break
    i=i+1   
print(ans)  