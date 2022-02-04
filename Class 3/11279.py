import heapq
import sys
n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    item = int(sys.stdin.readline())
    if item == 0:
        if heap:
            print(heapq.heappop(heap)*(-1))
        else:
            print(0)
    else:
        heapq.heappush(heap, -item)

