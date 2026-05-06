def outer_func(a, b):
    def inner_sum(x, y):
        return x + y
    
    total = inner_sum(a, b)
    return total + 5

result = outer_func(10, 20)
print(result)