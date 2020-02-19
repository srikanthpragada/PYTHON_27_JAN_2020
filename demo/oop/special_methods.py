class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property   # Getter method of property - h12
    def h12(self):
        if self.h > 12:
            return self.h - 12
        else:
            return self.h

    @h12.setter  # setter method of property - h12
    def h12(self, value):
        if value < 12:
            self.h = value

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def total_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __eq__(self, other):
        print("__eq__")
        return self.total_seconds() == other.total_seconds()

    def __gt__(self, other):
        print("__gt__")
        return self.total_seconds() > other.total_seconds()

    def __add__(self, other):
        return Time(self.h + other.h, self.m + other.m, self.s + other.s)

    def __int__(self):
        return self.total_seconds()


t1 = Time(20, 10, 10)
t1.h12 = 5
print(t1.h12)


t2 = Time(10, 10, 10)
print(t1)  # str(t1)  t1.__str__()
print(t1 == t2)
print(t1 != t2)
print(t1 > t2)  # t1.__gt__(t2)
print(t1 < t2)  # t1.__gt__(t2)
print(t1 + t2)
v = int(t1)  # t1.__int__()
print(type(v))
