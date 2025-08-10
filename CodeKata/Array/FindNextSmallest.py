a=[10,7,9,3,2,1,15] 
s=[]

# for i in range(len(a)-1):
#     small=float('inf')

#     for j in range(i+1,len(a)):
#         if a[j]<small:  
#             small=a[j]  
#             # s.append(small) 
#             break
#     if small == float('inf'):
#         s.append(-1)
#     else: 
#         s.append(small) 
 

# print(s) 
            

a = [10, 7, 9, 3, 2, 1, 15]
s = []

for i in range(len(a)):
    found = False
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            s.append(a[j])
            found = True
            break
    if not found:
        s.append(-1)

print(s)
