class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWait = 0
        end = -1
        for c in customers:
            end = max(c[0], end) + c[1]
            totalWait += end - c[0]
        
        return totalWait / len(customers)