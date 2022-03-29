def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return 'Found'
    return 'Not found'


if __name__ == '__main__':
    arr = [2, 6, 8, 9, 10, 11, 13]
    print(linear_search(arr, 2))
