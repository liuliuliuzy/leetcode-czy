def uniquePaths(m: int, n: int)->int:
    if m == 1 or n == 1:
        return 1
    res = 1
    M = m-1 + n-1
    N = min(m-1 , n-1)
    for i in range(N):
        res *= (M-i)
    for i in range(N):
        res /= i+1
    return int(res), res


if __name__ == "__main__":
    m = 9
    n = 8
    print(uniquePaths(m ,n))