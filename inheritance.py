class inherit1:
    def k(self):
        print("Hii")
class inherit2(inherit1):
    def l(self):
        print("Hello")
p=inherit2()
p.k()
p.l()