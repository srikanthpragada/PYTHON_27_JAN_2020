class A:
    def fun(self):
        print("Fun() in A")


class B:
    def fun(self):
        print("Fun() in B")


class C(A, B):
    pass

obj = C()
obj.fun()

