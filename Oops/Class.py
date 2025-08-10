class person():
    def __init__(self, fname,lname,age,education):
        self.fname=fname 
        self.lname=lname 
        self.age=age 
        self.education=education 
    
    def show(self):
        print("First Name:",self.fname)
        print("Last Name:",self.lname)
        print("Age:",self.age)
    
    def study(self):
        print("Qualification:",self.education)

a=person("Dilshad","Ansari",24,"CO Engineer") 
a.show()
# print(a.show())  
print(a.study())
