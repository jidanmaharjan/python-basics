# Heaps are a type of data structure that is used to implement priority queues.
# They can be implemented using lists in Python, where the first element is the smallest (min-heap) or largest (max-heap).
# Heaps are useful for efficiently finding the minimum or maximum element in a collection.

import heapq

minHeap = []
heapq.heappush(minHeap, 1)  # Add an element to the heap
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)  # Add another element to the heap

print(minHeap)  # Output: [1, 3, 2] (not sorted, but the smallest element is at the root)

heapq.heappush(minHeap, 0)  # Add another element to the heap
print(minHeap)  # Output: [0, 1, 2, 3] (0 is now the smallest element)

# Min is always at index 0
print(minHeap[0])  # Output: 0 (the smallest element)

# Pop the smallest element
smallest = heapq.heappop(minHeap)

print(smallest)  # Output: 0 (the smallest element is removed)
print(minHeap)  # Output: [1, 3, 2] (the heap is restructured)

heapq.heappush(minHeap, 4)  # Add another element to the heap

heapq.heappush(minHeap, 3) # Add another element to the heap
print(minHeap)  # Output: [1, 3, 2, 4, 3] (the heap is restructured)


# No max heaps by default in Python, but we can simulate it by pushing negative values
maxHeap = []
heapq.heappush(maxHeap, -1)  # Add an element to the max-heap (simulated)
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)  # Add another element to the max-heap (simulated)
print(maxHeap)  # Output: [-3, -1, -2] (not sorted, but the largest element is at the root)
heapq.heappush(maxHeap, 0)  # Add another element to the max-heap (simulated)
print(maxHeap)  # Output: [-3, -1, -2, 0] (0 is now the largest element in negative form)

# Max is always at index 0 (in negative form)
print(-maxHeap[0])  # Output: 3 (the largest element in positive form)

while maxHeap:
    largest = -heapq.heappop(maxHeap)  # Pop the largest element (in positive form)
    print(largest)  # Output: 3, 2, 1, 0 (the largest elements are removed in order)
    print(maxHeap)  # Output: [] (the heap is empty after all elements are popped)


# Build heap from initial values
arr= [5, 1, 3, 2, 4]
heapq.heapify(arr)  # Transform the list into a heap in-place
print(arr)  # Output: [1, 2, 3, 5, 4] (the list is now a heap)

