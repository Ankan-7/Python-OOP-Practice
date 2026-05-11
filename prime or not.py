class check_prime:
    def __init__(self,num):
        self.num=num
    def check_it(self):
        if self.num>1:
            for i in range(2,self.num):
                if self.num %i==0:
                    return "Not Prime"
            else:
                return "Prime"
        else:
            return "Not Prime"
"""    def display(self):
        result=self.check_it()
        print(result)
p=check_prime(2)
p.display()"""
p=check_prime(2)
result=p.check_it()
print(result)

            