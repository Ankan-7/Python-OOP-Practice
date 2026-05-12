class default_argu:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            d=a+b+c
            return d
        elif a!=None and b!=None and c==None:
            d=a+b
            return d
p=default_argu()
print(p.add(10,20,30))
print(p.add(10,20))