def binary_search(arr, num):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if num < arr[mid]:
            hi = mid-1
        elif num > arr[mid]:
            lo = mid+1
        elif num == arr[mid]:
            print(num, 'found in array.')
            break
    if lo > hi:
        print(num, 'is not present in the array!')


if __name__ == '__main__':
    arr = [2, 6, 8, 9, 10, 11, 13]
    binary_search(arr, 12)
