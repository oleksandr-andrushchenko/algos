# A queue is a data structure that follows the First In, First Out (FIFO) principle.

from collections import deque

queue = deque()

queue.append(1)
print('queue.append(1) ->', list(queue))

queue.append(2)
print('queue.append(2) ->', list(queue))

queue.append(3)
print('queue.append(3) ->', list(queue))

print('queue.pop() ->', queue.pop(), list(queue))

print('queue.popleft() ->', queue.popleft(), list(queue))

queue.appendleft(4)
print('queue.appendleft(4) ->', list(queue))

# FIFO (Queue) vs. LIFO (Stack)

# Queue (FIFO - First In, First Out)
#
# Elements are added to the back and removed from the front.
# ✅ Correct way: queue.append(x) (enqueue), queue.popleft() (dequeue).

# Stack (LIFO - Last In, First Out)
#
# Elements are added to the top and removed from the top.
# ✅ Correct way: stack.append(x) (push), stack.pop() (pop).

print('Queue (FIFO): queue.append(x) (enqueue), queue.popleft() (dequeue)')
print('Stack (LIFO): stack.append(x) (push), stack.pop() (pop)')
