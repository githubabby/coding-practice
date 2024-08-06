"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
# IndexError: list index out of range

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j = m-1, n-1
    k = m+n-1
    while j>=0:
        if i>=0 and nums1[i]>=nums2[j]: # I got index error coz i forgot to check if i is less than 0
            nums1[k] = nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1

if __name__=="__main__":
    test_cases = [
        {
            'nums1':[1,2,3,0,0,0],
            'm':3,
            'nums2':[2,5,6],
            'n':3
        },
        {
            'nums1':[1],
            'm':1,
            'nums2':[],
            'n':0
        },
        {
            'nums1':[0],
            'm':0,
            'nums2':[1],
            'n':1
        }
    ]
    test_results = [
        [1,2,2,3,5,6],
        [1],
        [1]
    ]
    for i in range(len(test_cases)):
        merge(test_cases[i]["nums1"], test_cases[i]["m"], test_cases[i]["nums2"], test_cases[i]["n"])
        assert test_cases[i]["nums1"] == test_results[i]