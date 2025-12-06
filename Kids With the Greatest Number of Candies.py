def maxCandies(self, candies: List[int]):
        max = candies[0]
        for i in candies:
            if i>max:
                max=i
        return max
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max = self.maxCandies(candies)
        for i in candies:
            if i+extraCandies>=max:
                res.append(True)
            else:
                res.append(False)

        return res
