class A:
    def fun(self):
        print("Fun() in A")


class B:
    def process(self):
        print("Process() in B")


class C(A, B):
    def fun(self):
        print("Fun() in C")


obj = C()
obj.fun()
obj.process()
