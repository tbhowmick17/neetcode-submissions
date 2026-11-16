class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [0] * len(nums) 
        prod, zeros = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zeros += 1
        if zeros > 1: return [0] * len(nums)

        for i, c in enumerate(nums):
            if zeros: prods[i] = 0 if c else prod
            else:
                prods[i] = prod // c

        return prods