n=int(input())

li=list(map(int,input().split()))
sum=0
for i in range(n):
    sum=sum+li[i]
# print(sum)
if sum%2==0 and sum%3==0 and sum%5==0:
    print(1)
else:
    print(0)