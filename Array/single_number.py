def singleNumber(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res
        
singleNumber([2,2,1])