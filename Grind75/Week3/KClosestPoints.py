import heapq

class KClosestPoints:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def square_sum(x: int, y: int) -> float:
            return x*x + y*y

        heap = [[square_sum(x, y), x, y] for x, y in points]
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            sq, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res
