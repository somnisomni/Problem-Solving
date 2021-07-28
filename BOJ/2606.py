class Node:
    def __init__(self, n):
        #self.index = n
        self.subnodes = []
        self.visited = False

    def infect(self):
        #print("[", self.index, "]", [node.index for node in self.subnodes])
        self.visited = True

        for node in self.subnodes:
            if node.visited == False:
                node.infect()

N, L = int(input()), int(input())
nodeList = [None] + [Node(i + 1) for i in range(N)]

for _ in range(L):
    i, j = map(int, input().split())

    nodeList[i].subnodes.append(nodeList[j])
    nodeList[j].subnodes.append(nodeList[i])

nodeList[1].infect()

infectedCount = 0
for n in range(1, N + 1):
    if nodeList[n].visited == True:
        infectedCount += 1

#print()
print(infectedCount - 1)
