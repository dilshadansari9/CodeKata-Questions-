path='D:\\Guvi\\File Handling\\New.txt'

file=open(path,'r')
# print(file.name)
# print(file.mode)
# print(file.read())
# print(file.readline())

# The better way of opening a file is using with keyword 


with open(path,'r') as f:
    # file_c=file1.read()
    # print(file_c)
    # print(f.read(4)) # This will read first four characters 
    # print("first line: " + f.readline()) # This will read first line 
    # print("first line: " + f.readline(4))  #This will read the first 4 character     

    # we can also iterate through a file 

    i=0
    for line in f:
        print("Iteration ",i,": ", line )
        i+=1
    
#We can store file in the another variable and print them line by line. 
with open(path,'r') as f:
    f1=f.readlines()
print(f1[0])
print(f1[1])
print(f1[2])
