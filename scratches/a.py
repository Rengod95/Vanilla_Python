class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second

    def minus(self):
        return self.first - self.second

    def div(self):
        return self.first/self.second

    def mul(self):
        return self.first*self.second

a, b = map(int, input().split())

test1 = Calculator(a,b)

print(test1.add())
print(test1.minus())
print(test1.div())
print(test1.mul())