def sum_recursion(n):
    if n <= 1:
        return n
    return n + sum_recursion(n - 1)

print(sum_recursion(10)) 