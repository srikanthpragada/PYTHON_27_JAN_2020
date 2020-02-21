class A:
    def __init__(self, v1):
        self.v1 = v1
        print("Constructor in A")


class B:
    def __init__(self, v2):
        self.v2 = v2
        print("Constructor in B")


class C(B, A):
    def __init__(self):
        A.__init__(self, 10)
        B.__init__(self, 20)
        print(self.v1, self.v2)


obj = C()
