import heapq
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_heap = defaultdict(list)
        self.number_to_active = defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number != number:
                self.number_to_active[old_number].discard(index)
        self.index_to_number[index] = number
        self.number_to_active[number].add(index)
        heapq.heappush(self.number_to_heap[number], index)

    def find(self, number: int) -> int:
        heap = self.number_to_heap[number]
        active = self.number_to_active[number]
        while heap and heap[0] not in active:
            heapq.heappop(heap)
        return heap[0] if heap else -1
