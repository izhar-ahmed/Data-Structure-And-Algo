# my fist solution
# def maxWaterContainer(heights):
#     max = 0
#     for i in range(len(heights)):
#         dist = 0
#         for j in range(i + 1, len(heights)):
#             dist += 1
#             if heights[i] < heights[j]:
#                 if heights[i] * dist > max:
#                     max = heights[i] * dist
#                 else:
#                     continue
#             elif heights[j] < heights[i]:
#                 if heights[j] * dist > max:
#                     max = heights[j] * dist
#                 else:
#                     continue
#             else:
#                 if heights[i] * dist > max:
#                     max = heights[i] * dist
#                 else:
#                     continue
#     return max

# print(maxWaterContainer([1,8,6,2,5,4,8,3,7]))

class Solution():
    def maxArea(self, height):
        self.height = height
        l = 0
        r = len(self.height) - 1
        max = 0
        dist = len(self.height) - 1
        while l < r:
            if self.height[l] < self.height[r] or self.height[l] == self.height[r]:
                if self.height[l] * dist > max:
                    max = self.height[l] * dist
                    l += 1
                    dist -= 1
                else:
                    l += 1
                    dist -= 1
            else:
                if self.height[r] * dist > max:
                    max = self.height[r] * dist
                    r -= 1
                    dist -= 1
                else:
                    r -= 1
                    dist -= 1
        return max

mySolution = Solution()
print(mySolution.maxArea([1,8,6,2,5,4,8,3,7]))


