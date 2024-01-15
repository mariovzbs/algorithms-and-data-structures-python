class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.heapify(largest)

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)

        return max_value


heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(15)
heap.insert(30)

print(heap.heap)
print(heap.extract_max())
print(heap.heap)
