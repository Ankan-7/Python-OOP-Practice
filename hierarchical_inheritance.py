#Hierarchical Inheritance
class inherit1:
    def __init__(self,name):
        self.name=name
    def k(self):
        print("Hii",self.name)
class inherit2(inherit1):
    def l(self):
        print("Hello",self.name)
class inherit3(inherit1):
    def m(self):
        print("Heyy",self.name)
p=inherit2("Ankan")
q=inherit3("ankan")
p.k()
p.l()
q.k()
q.m()