def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            runningSum.append(sum)

        return runningSum
