n=int(input())

prev=1 
sec_prev=-1
a=[]
for i in range(n):
    next_no=prev+sec_prev 
    sec_prev=prev 
    prev=next_no 
    a.append(str(next_no))
print(" ".join(a))