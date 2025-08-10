s='I am shrey '
# a=list(s) 
print(len(s))    
i=0  
low=['a','e','i','o','u']
cap=['A','E','I','O','U']
 
while i <len(s):
    if s[i] in low or s[i] in cap:
        s=s[:i]+s[i+1:]
    else:
        i=i+1 
print(s) 
