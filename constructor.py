class c:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
p1=c("Ankan",21)
print(p1.name,p1.age)
p1.display()