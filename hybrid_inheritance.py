#Hybrid Inheritance(Multilevel,Multiple)
class A:
    def __init__(self,name):
        self.name=name
    def moja(self):
        print("Hello",self.name)
class B(A):
    def sei_moja(self):
        print("Hii",self.name)
class D:
    def __init__(self,name):
        self.name=name
    def sei_sei_moja(self):
        print("Heyy",self.name)
class C(B,D):
    def sei_moja_returns(self):
        print("Holaa",self.name)
p=C("Ankan")
p.moja()
p.sei_moja()
p.sei_sei_moja()
p.sei_moja_returns()