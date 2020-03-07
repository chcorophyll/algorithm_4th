import numpy as np


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def binary_search(key, arr):
    low = 0
    high = len(arr) - 1
    mid = (low + high) / 2 + 1
    while low <= high:
        if key < arr[mid]:
            high = mid -1
        elif key > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

# 1.1.13
def array_transposed(arr):
    assert len(arr.shape) == 2
    m = arr.shape[0]
    n = arr.shape[1]
    temp = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            temp[j, i] = array[i, j]
    return temp

# 1.1.14
def my_log(num):
    assert isinstance(num, int)
    count = 0
    while num >= 2:
        num -= 2
        count += 1
    return count
# def my_log(num):
#     i = 1
#     j = -1
#     while i <= num:
#         i *= 2
#         j += 1
#     return j

# 1.1.15
def histogram(arr, m):
    temp = [0] * len(m)
    for i in range(m):
        for j in range(len(arr)):
            if arr[j] == i and 0 <= arr[j] < m:
                temp[i] += 1
    return temp

# 1.1.20
def log_factorial(num):
    if num == 0 or num == 1:
        return 0
    else:
        return np.log(num) + log_factorial(num - 1)

# 1.1.22
def binary_search_record(key, arr, depth=1):
    low = 0
    high = len(arr) - 1
    mid = (low + high) / 2 + 1
    print("\t" * depth, "low:", low, "high:", high)
    while low <= high:
        if key < arr[mid]:
            depth += 1
            temp = [arr[i] for i in range(mid - 1)]
            return binary_search_record(key, temp, depth)
        elif key > arr[mid]:
            depth += 1
            temp = [arr[i] for i in range(mid + 1, high + 1)]
            return binary_search_record(key, temp, depth)
        else:
            return mid
    return -1

# 1.1.24
def gcd_record(a, b, record=None):
    if not record:
        record = []
    record.append((a, b))
    if b == 0:
        return a, record
    return gcd(b, a % b, record)

# 1.1.26
def sort_3_num(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c

# 1.1.29
def binary_search_rank(key, arr):
    low = 0
    high = len(arr) - 1
    mid = (low + high) - 1
    count = 0
    while low <= high:
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        else:
            while arr[mid] == key:
                mid -= 1
                count += 1
            return mid, count
    return -1, count





