# This question is designed to help you get a better understanding of basic heap operations.
#
# There are  types of query:
#
# " " - Add an element  to the heap.
# " " - Delete the element  from the heap.
# "" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap.
# Also, at any instant, only distinct elements will be in the heap.

import heapq

if __name__ == "__main__":
    q = int(input().strip())
    heap = []
    removed = set()
    heapq.heapify(heap)
    for _ in range(q):
        cmd = input().strip().split()
        if cmd[0] == "1":
            heapq.heappush(heap, int(cmd[1]))
        elif cmd[0] == "2":
            # heap.remove(int(cmd[1]))
            # heapq.heapify(heap)
            removed.add(int(cmd[1]))
        elif cmd[0] == "3":
            while heap and heap[0] in removed:
                removed.remove(heapq.heappop(heap))
            print(heap[0])
