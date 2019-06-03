class oo:
    def sum(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def comparison(self):
        a=int(input())
        b=int(input())
        if(a==b):
            print("a and b are equal")
        else:
            print("values are not equal")
    def identity(self):
        try:
            a = int(input())
            if type(a) is int:
                print("value is int")
        except Exception:
             print("value is not int")
    def membership(self):
        a="hello"
        if "hell" in a:
            print("string found")
        else:
            print("string not found")
    def logical(self):
        a=int(input())
        b=int(input())
        c=int(input())
        if(a==b and b==c):
            print("a,b,c are equal")
        else:
            print("a,b,c are not equal")
o=oo()
print(o.sum(2,3))
print(o.subtract(10,5))
print(o.comparison())
print(o.identity())
print(o.membership())
print(o.logical())
