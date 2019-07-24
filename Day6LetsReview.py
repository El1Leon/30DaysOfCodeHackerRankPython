NumberOfTestCases = int(input())
for i in range(NumberOfTestCases):
    TestString = input()
    EvenIndexedCharacters = ""
    OddIndexedCharacters = ""
    for j in range(len(TestString)):
        if j % 2 == 0:
            EvenIndexedCharacters += TestString[j]
        if j %2 != 0:
            OddIndexedCharacters += TestString[j]
    print("{0} {1}".format(EvenIndexedCharacters, OddIndexedCharacters))
print("")
