Aapple, Aorange = map(int, input().split())
Bapple, Borange = map(int, input().split())

print(min(Bapple + Aorange, Aapple + Borange))
