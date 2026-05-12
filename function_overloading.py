class overload:
    def add(self,a,b):
        x=a+b
        return x
    def add(self,a,b,c):
        d=a+b+c
        return d
p=overload()
print(p.add(10,20,30))
print(p.add(10.20))