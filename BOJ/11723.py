import sys
input = sys.stdin.readline

array = set()

for _ in range(int(input().rstrip())):
    com = input().split()
    arg = -1

    if len(com) == 2:
        arg = int(com[1])
    com = com[0]

    if arg == -1:
        if com == "all":
            array = set([n for n in range(1, 21)])
        elif com =="empty":
            array = set()
    else:
        if com == "add":
            array.add(arg)
        elif com == "remove":
            if array & set([arg]):
                array.remove(arg)
        elif com =="check":
            if array & set([arg]): print(1)
            else: print(0)
        elif com =="toggle":
            if array & set([arg]): array.remove(arg)
            else: array.add(arg)