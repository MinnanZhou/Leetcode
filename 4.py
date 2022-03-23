def findMedianSortedArrays(nums1, nums2) -> float:
    m = len(nums1)
    n = len(nums2)
    total=m+n
    so = []
    if m==0:
        so=nums2
    elif n==0:
        so=nums1
    else:
        for i in range(m + n):
            if nums1[m - 1] >= nums2[n - 1]:
                so.append(nums1[m - 1])
                m -= 1
                if m == 0:
                    m += 1
                    nums1[0] = -1
            else:
                so.append(nums2[n - 1])
                n -= 1
                if n == 0:
                    n += 1
                    nums2[0] = -1
    if total % 2 == 0:
        po = total // 2
        return 0.5 * (so[po] + so[po - 1])
    else:
        return so[total // 2]


input1 = []
input2 = [3]
z = findMedianSortedArrays(input1, input2)
print(z)
