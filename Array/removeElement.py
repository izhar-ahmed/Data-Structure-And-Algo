class Solution():
    def removeElement(self, nums, val):
        self.nums = nums
        self.val = val
        arr = []
        k = 0
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == self.val:
                count += 1
            else:
                k += 1
                arr.append(self.nums[i])
        for i in range(count):
            arr.append(1)
        for i in range(len(arr)):
            self.nums[i] = arr[i]
        return k

mySolution = Solution()
mySolution.removeElement([0,1,2,2,3,0,4,2], 2)