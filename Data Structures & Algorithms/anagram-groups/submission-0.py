class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}

        for s in strs:
            s_list = list(s)
            s_list.sort()
            sorted_str = ''.join(s_list)
            if sorted_str in mapper:
                mapper[sorted_str].append(s)
            else:
                mapper[sorted_str] = [s]

        return list(mapper.values())
