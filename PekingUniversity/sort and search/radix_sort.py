def radix_sort(a_list):
    n = len(a_list)
    if n < 2:
        return a_list
    max_value = float("-inf")
    for i in range(n):
        max_value = max(max_value, a_list[i])
    exp = 1
    buffer_list = [0] * n
    while max_value >= exp:
        level_count = [0] * 10
        for i in range(n):
            digit = (a_list[i] // exp) % 10
            level_count[digit] += 1
        for i in range(1, 10):
            level_count[i] += level_count[i-1]
        for i in range(n-1, -1, -1):
            digit = (a_list[i] // exp) % 10
            buffer_list[level_count[digit]-1] = a_list[i]
            level_count[digit] -= 1
        a_list = buffer_list[:]
        exp *= 10
    return a_list


if __name__ == "__main__":
    a_list = [3, 2, 5, 1, 0, 4]
    print(radix_sort(a_list))