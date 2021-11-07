import sys
from queue import deque

input = sys.stdin.readline

queue = deque()

for _ in range(int(input())):
  command = input().rstrip()

  if command.startswith("push"):
    command, val = command.split()
    val = int(val)

    queue.append(val)
  elif command == "pop":
    print(queue.popleft() if len(queue) > 0 else -1)
  elif command == "size":
    print(len(queue))
  elif command == "empty":
    print(1 if len(queue) == 0 else 0)
  elif command == "front":
    print(queue[0] if len(queue) > 0 else -1)
  elif command == "back":
    print(queue[-1] if len(queue) > 0 else -1)
