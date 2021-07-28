class Node:
    def __init__(self, index):
        self.index = index
        self.linkedNodes = []
        self.visited = False

    def processDFS(self, allNodeNumericList, count = 0):
        self.visited = True
        allNodeNumericList.remove(self.index)
        count += 1

        for node in self.linkedNodes:
            if node.visited == False:
                count = node.processDFS(allNodeNumericList, count)
        
        return count
        

N, M = map(int, input().split())
nodeList = [None] + [Node(i) for i in range(1, N + 1)]
maxFriends = 1

for _ in range(M):
    u, v = map(int, input().split())

    nodeList[u].linkedNodes.append(nodeList[v])
    nodeList[v].linkedNodes.append(nodeList[u])

nodeListNumeric = list(range(1, N + 1))

while nodeListNumeric:
    count = nodeList[nodeListNumeric[0]].processDFS(nodeListNumeric)
    maxFriends = max(maxFriends, count)

print(maxFriends)
