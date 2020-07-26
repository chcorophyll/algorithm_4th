import copy


def factorial(n):
    if n == 1:
        return 0
    else:
        return n * factorial(n-1)


def reverse_list(list_input):
    if len(list_input) == 1:
        return list_input
    else:
        return [list_input[-1]] + reverse_list(list_input[:-1])


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_iteration(n):
    result = []
    a = 0
    b = 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


def bottle_problem(x, y, z):
    if x < y:
        x, y = y, x
    if y - x == z:
        return True
    if x == 0:
        return False
    # 先倒满大瓶
    bottle_a = y
    bottle_b = 0
    # 从大瓶倒满小瓶
    bottle_a = y - x
    bottle_b = x
    if bottle_a == z:
        return True
        return bottle_problem(2*x-y, y, z)


def package_problem(item_list, value_list, m):
    dp = [0] * (m + 1)
    dp = [dp] * (len(item_list) + 1)
    # base case
    # item and value choice
    for i in range(1, len(item_list) + 1):
        for j in range(1, m+1):
            if value_list[i-1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - value_list[i-1]] + value_list[i-1])
    return dp[len(item_list)][len(value_list)]

def package_problem_recursion(item_list, value_list, m):
    # base case
    if len(item_list) == 0:
        return 0
    if m == 0:
        return 0
    res = 0
    for i in range(1, len(item_list)+1):
        new_item_list = copy.deepcopy(item_list).pop(i-1)
        new_value_list = copy.deepcopy(value_list).pop(i-1)
        res = max(res, package_problem(new_item_list, new_value_list, m-value_list[i-1]) + value_list[i-1])
    return res


def package_problem_recursion(item_list, value_list, m):
    memo = [0] * (m+1)
    def re(item_temp, value_temp, m_temp)
        # base case
        if len(item_list) == 0:
            return 0
        if m == 0:
            return 0
        if memo[m] != 0:
            return memo[m]
        res = 0
        for i in range(1, len(item_temp)+1):
            new_item_list = copy.deepcopy(item_temp).pop(i-1)
            new_value_list = copy.deepcopy(value_temp).pop(i-1)
            memo[m-value_list[i-1]] = re(new_item_list, new_value_list, m-value_list[i-1]) + value_temp[i-1]
            res = max(res, re(new_item_list, new_value_list, m-value_list[i-1]) + value_temp[i-1])
        return res
    return re(item_list, value_list, m)


def word_edict(word_1, word_2):
    def dp(i, j):
        # base case
        if i == -1 :
            return j + 1
        if j == -1:
            return i + 1
        if word_1[i] == word_2[j]:
            return dp(i-1, j-1)
        else:
            return min(dp(i-1, j) + 1, dp(i, j-1)+1, dp(i-1, j-1)+1)
    return dp(len(word_1)-1, len(word_2)-2)

def word_edict(word_1, word_2):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        # base case
        if i == -1 :
            # memo[(i, j)] = j + 1
            return j + 1
        if j == -1:
            # memo[(i, j)] = i + 1
            return i + 1
        if word_1[i] == word_2[j]:
            memo[(i, j)] = memo[(i-1, j-1)]
        else:
            memo[(i, j)] = min(dp(i-1, j) + 1, dp(i, j-1)+1, dp(i-1, j-1)+1)
        return memo[(i, j)]
    return dp(len(word_1)-1, len(word_2)-2)

def word_edict(word_1, word_2):
    m = len(word_1) + 1
    n = len(word_2) + 1
    dp = [0] * n
    dp = [dp] * m
    # base case
    for i in range(1, m):
        dp[i][0] = i
    for j in range(1, n):
        dp[0][j] = j
    for i in range(1, m):
        for j in range(1, n):
            if word_1[i] == word_2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
    return dp[m-1][n-1]





if __name__ == "__main__":
    print(factorial(1))
    print(reverse_list([1, 2, 3, 4]))
    print(fibonacci(4))
    print(fibonacci_iteration(4))
