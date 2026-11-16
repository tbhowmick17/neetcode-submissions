class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for n in nums:
            # check if n is the start of sequence
            if (n-1) in num_set:
                continue
            else:
                length = 0
                while (n + length) in num_set:
                    length += 1
                max_seq = max(max_seq, length)

        return max_seq