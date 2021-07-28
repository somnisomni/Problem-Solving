N = int(input())
targetA, targetB = map(int, input().split())
M = int(input())

allParentA = []
allParentB = []

class Node:
    def __init__(self, index):
        self.index = index
        self.parent = None
    
    def visitAllParents(self, parentList):
        parentList.insert(0, self.index)

        if self.parent != None:
            self.parent.visitAllParents(parentList)

peoples = [None] + [Node(i) for i in range(1, N + 1)]

# Relation input
for _ in range(M):
    x, y = map(int, input().split())

    peoples[y].parent = peoples[x]

# Process bottom-up ancestor finding
peoples[targetA].visitAllParents(allParentA)
peoples[targetB].visitAllParents(allParentB)

# Get common ancestor
allParentASet = set(allParentA)
allParentBSet = set(allParentB)

commonParent = -1

if len(allParentASet & allParentBSet) >= 1:
    commonParent = list(allParentASet & allParentBSet)[-1]

# Print
if commonParent == -1:
    # No common ancestor
    print(-1)
else:
    # Get length to common ancestor
    lengthA = len(allParentA) - allParentA.index(commonParent) - 1
    lengthB = len(allParentB) - allParentB.index(commonParent) - 1

    print(lengthA + lengthB)