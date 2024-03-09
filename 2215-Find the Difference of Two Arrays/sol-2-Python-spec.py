class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setOfnums1 = set(nums1)
        setOfnums2 = set(nums2)
        resultSet1, resultSet2 = set(), set()
        
        for n in nums1:
            if n not in setOfnums2:
                resultSet1.add(n)

        for n in nums2:
            if n not in setOfnums1:
                resultSet2.add(n)

        return[list(resultSet1), list(resultSet2)]  
