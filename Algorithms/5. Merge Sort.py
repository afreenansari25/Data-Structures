# Time Complexity: O(nlogn)

def merge(nums1, nums2):
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged+nums1[i:]+nums2[j:]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    return merge(left_sorted, right_sorted)


nums = [6, 1, 3, 7, 9, 2, 0]
print(merge_sort(nums))