class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(a) > len(b):
            a, b = b, a

        l, r = 0, len(a) - 1

        while True:
            midA = (l + r) // 2
            midB = half - midA - 2

            leftA = a[midA] if midA >= 0 else float("-infinity")
            rightA = a[midA+1] if (midA+1) < len(a) else float("infinity")

            leftB = b[midB] if midB >=0 else float("-infinity")
            rightB = b[midB+1] if (midB+1) < len(b) else float("infinity")

            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = midA - 1
            else:
                l = midA + 1 