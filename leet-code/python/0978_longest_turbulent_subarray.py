class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSpace = curSpace = 1
        increase = True
        for i in range(1, len(arr)):
            curSpace += 1

            if curSpace == 2:
                increase = arr[i - 1] < arr[i]

            if arr[i - 1] < arr[i] and increase or arr[i - 1] > arr[i] and not increase:
                increase = not increase
            else:
                curSpace = 2 if arr[i - 1] != arr[i] else 1

            maxSpace = max(maxSpace, curSpace)
        
        return maxSpace

