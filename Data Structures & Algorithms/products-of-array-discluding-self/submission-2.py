class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [0] * len(nums)
        prod, zeroes = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zeroes += 1
        if zeroes > 1: 
            return prods

        for i, num in enumerate(nums):
            if zeroes:
                prods[i] = 0 if num else prod
            else:
                prods[i] = prod // num

        return prods
