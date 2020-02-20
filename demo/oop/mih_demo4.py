class A:
    def fun1(self):
        print("Fun() in A")

class B(A):
    pass

class C:
    def fun(self):
        print("Fun() in C")

class D(B,C):
    pass

obj = D()
obj.fun()

