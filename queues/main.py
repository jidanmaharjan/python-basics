# Queues are double-ended queues that allow adding and removing elements from both ends.
from collections import deque
queue = deque()

queue.append(1)  # Add to the right end
queue.append(2)  # Add to the right end

print(queue)  # deque([1, 2])

queue.popleft()
print(queue)  # deque([2])

queue.appendleft(3)  # Add to the left end
print(queue)  # deque([3, 2])   

queue.pop()  # Remove from the right end
print(queue)  # deque([3])