from heapq import heappush, heappop


class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def medianSlidingWindow(self, nums, k):
        result = []
        for i in range(len(nums)):
            self.rebalance(nums, i)
            if i >= k - 1:
                if k % 2 == 0:
                    result.append(self.minHeap[0] / 2 - self.maxHeap[0] / 2)
                else:
                    result.append(-self.maxHeap[0])
                toRemove = nums[i - k + 1]
                if toRemove <= - self.maxHeap[0]:
                    self.remove(self.maxHeap, -toRemove)
                else:
                    self.remove(self.minHeap, toRemove)
                self.rebalance(nums, i)
        return result

    def remove(self, heap, ele):
        idn = heap.index(ele)
        heap[idn] = heap[-1]
        del heap[-1]
        if idn < len(heap):
            heap._siftup(heap, idn)
            heap._siftdown(heap, 0, idn)

    def rebalance(self, nums, i):
        heappush(self.maxHeap, -nums[i])
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


print(Solution.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
