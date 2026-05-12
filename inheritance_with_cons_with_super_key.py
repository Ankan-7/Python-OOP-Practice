class inherit1:
    def __init__(self,name):
        self.name=name
    def k(self):
        print("Hii",self.name)
class inherit2(inherit1):
    def l(self):
        super().k()
        print("Hello",self.name)
p=inherit2("Ankan")
#p.k()
p.l()