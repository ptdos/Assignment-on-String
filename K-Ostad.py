def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def is_k_ostad(str1, str2, k):
    if str1 == str2:
        return True

    distance = edit_distance(str1, str2)

    if distance <= k:
        return True

    return False


# Test cases
str1 = "anagram"
str2 = "grammar"
k = 3
print(is_k_ostad(str1, str2, k))  # Output: Yes

str1 = "ostad"
str2 = "boss"
k = 1
print(is_k_ostad(str1, str2, k))  # Output: No
