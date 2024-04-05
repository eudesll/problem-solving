class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    # return sorted(nums)
    return self.mergeSort(nums, 0, len(nums) - 1)
    
    # Insertion sort - n * n
    for i in range(1, len(nums)):
      j = i - 1
      while j >= 0 and nums[j + 1] < nums[j]:
        tmp = nums[j + 1]
        nums[j + 1] = nums[j]
        nums[j] = tmp
        j -= 1
    return nums

  # Merge sort - n * log(n)
  def mergeSort(self, arr, s, e):
    if e - s + 1 <= 1:
        return arr

    m = (s + e) // 2

    self.mergeSort(arr, s, m)
    self.mergeSort(arr, m + 1, e)

    self.merge(arr, s, m, e)
    
    return arr

  def merge(self, arr, s, m, e):
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i, j = 0, 0
    k = s

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1