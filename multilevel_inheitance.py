#Multilevel Inheritance
class inherit1:
    def __init__(self,name):
        self.name=name
    def k(self):
        print("Hii",self.name)
class inherit2(inherit1):
    def l(self):
        print("Hello",self.name)
class inherit3(inherit2):
    def m(self):
        print("Hey",self.name)
p=inherit3("Ankan")
p.k()
p.l()
p.m()
