'''
295. Find Median from Data Stream

https://leetcode.com/problems/find-median-from-data-stream/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

'''
from heapq import heappush, heappop

# make minHeap one number more than maxHeap
# minHeap stores the larger half of the numbers


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        return self.minHeap[0]
# time complexity: O(logn), space complexity: O(n)


'''
480. Sliding Window Median
https://stackoverflow.com/questions/68510425/removing-value-from-heap-why-siftup-and-siftdown-need-to-be-called

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
'''

# not working solution


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

# time complexity O(n * k) Space O(n)

# AttributeError: 'list' object has no attribute '_siftup'
#     heap._siftup(heap, idn)


'''
502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
'''
