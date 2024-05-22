def man(n, m):
    res = 1
    if m > n - m:
        m = n - m
    for i in range(0, m):
        res *= (n - i)
        res /= (i + 1)
    return res
def calculate(n, m):
    if n<m:
        return 0
    ways = man(m + n-1, m-1)
    return int(ways)
if __name__ == '__main__':
    n = 7 ;m = 5

    result = calculate(n, m)
    print(result)


