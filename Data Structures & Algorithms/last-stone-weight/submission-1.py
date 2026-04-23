class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x == y:
                continue
            elif x < y:
                y = -(y-x)
                heapq.heappush(maxHeap, y)
            elif y < x:
                x = -(x-y)
                heapq.heappush(maxHeap, x)
        
        if len(maxHeap) == 0:
            return 0
        return -maxHeap[0]


