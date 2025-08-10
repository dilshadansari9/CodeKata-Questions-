# li=[1,1,2,2,4,5,5]
# num=0 
# for i in range(len(li)):
#     for j in range(i+1,len(li)) :
#         if li[j]!=li[i]:
#             # print(li[i]) 
#             num=li[j] 
#         print(num)
#             # break

a=[1,2]
b=[2,3,1]
print(a+b)  
b.sort(reverse=True)
print(b)  
for i in b: 

    a.append(i) 

print(" ".join(a))  
print(a) 