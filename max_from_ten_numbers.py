class check_max:
    def __init__(self,num):
        self.num=num
    def check_it(self):
        print("Enter 10 numbers:")
        for i in range(1,10):
            curr=eval(input("Enter a number :"))
            if curr>self.num:
                self.num=curr
        return self.num
p=check_max(3)
result=p.check_it()
print(result)