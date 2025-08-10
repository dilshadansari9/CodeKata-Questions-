with open (r"D:\Guvi\File Handling\New2.txt",'w') as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n") 
line=['THis is line 4\n','THis is line 5\n','THis is line 6\n']
with open (r"D:\Guvi\File Handling\New2.txt",'w') as file:
    for i in line:
        file.write(i) 