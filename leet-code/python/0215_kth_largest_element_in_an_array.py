class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    def quickselect(nums, k):
        small, equal, large = [], [], []
        pivot = random.choice(nums)
        for num in nums:
            if num > pivot:
                large.append(num)
            elif num == pivot:
                equal.append(num)
            elif num < pivot:
                small.append(num)

        # CASE-1
        if len(large) >= k:
            # means kth largest element is present in large array
            return quickselect(large, k)

        # CASE-2
        elif (len(large) + len(equal))  < k:
            # this means k-th largest element is in small array
            return quickselect(small, k-(len(large) + len(equal)))

        # CASE-3
        else:
            # pivot (and all elems. in equal) e j aapno k-th largest number chhe.
            return pivot
    return quickselect(nums, k)
      
    heap = nums[:k]
    heapq.heapify(heap)
    
    for i in range(k, len(nums)):
      if heap[0] < nums[i]:
        heapq.heappushpop(heap, nums[i])
      
    return heap[0]