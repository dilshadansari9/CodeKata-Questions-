arr = [1, 2, 3, 4, 5, 6,5,6,2,8]
# Output: Even: 3, Odd: 3

even=0 
odd=0

for i in arr:
    if i%2==0:
        even+=1 
    else:
        odd+=1 
print("Even: ",even)
print("Odd: ",odd)