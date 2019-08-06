import sys

n = int(input().strip())
phoneBook = dict()

for i in range(n):
    name = sys.stdin.readline().strip().split(" ")
    phoneBook[name[0]] = name[1]
query = sys.stdin.readline().strip()
while query:
    phoneNumber = phoneBook.get(query)
    if phoneNumber:
        print(query + '=' + phoneNumber)
    else:
        print('Not Found')
    query = input().strip()


