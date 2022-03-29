# Time complexity: O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


nums = [6, -5, 2, 1, -9, 3, 4, 10000, 100]
print(bubble_sort(nums))