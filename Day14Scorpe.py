class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        minimumElement = 101
        maximumElement = 0
        for element in self.__elements:
            if element < minimumElement:
                minimumElement = element
            if element > maximumElement:
                maximumElement = element

        self.maximumDifference = maximumElement - minimumElement

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)