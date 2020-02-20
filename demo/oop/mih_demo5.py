class A:
    def fun(self):
        print("Fun() in A")

class B(A):
    pass

class C(A):
    def fun(self):
        print("Fun() in C")

class D(B,C):
    pass

obj = D()
obj.fun()
print(D.mro())

