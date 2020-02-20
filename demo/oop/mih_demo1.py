class A:
    def fun(self):
        print("Fun() in A")


class B:
    def process(self):
        print("Process() in B")


class C(A, B):
    pass


obj = C()
obj.fun()
obj.process()
