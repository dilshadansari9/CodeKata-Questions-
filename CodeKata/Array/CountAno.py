# n=int(input())
# a=list(map(int,input().split()))

a=[1,3,7,3,1,8,7]
result = 0

for i in range(32):
    bit_sum = 0
    
    for num in a:
        if (num >> i) & 1:
            bit_sum += 1

    if bit_sum % 3 == 2:
        result |= (1 << i)

if (result >> 31) & 1:
    result -= 1 << 32

print(result)  
