N, M = map(int, input().split())
nodeListNumeric = list(range(1, N + 1))

class Node:
    def __init__(self, index):
        self.index = index
        self.linkedNodes = []
        self.visited = False

    def processDFS(self):
        global nodeListNumeric

        self.visited = True
        nodeListNumeric.remove(self.index)
        #print(nodeListNumeric)

        for node in self.linkedNodes:
            if node.visited == False:
                node.processDFS()

nodeList = [None] + [Node(i) for i in range(1, N + 1)]
connectedComponents = 0

for _ in range(M):
    u, v = map(int, input().split())

    nodeList[u].linkedNodes.append(nodeList[v])
    nodeList[v].linkedNodes.append(nodeList[u])

while nodeListNumeric:
    #print("Start DFS at", nodeListNumeric[0])
    nodeList[nodeListNumeric[0]].processDFS()
    connectedComponents += 1

print(connectedComponents)
