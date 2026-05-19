def sum_of(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total

print(sum_of(a=1, b=2, c=3))  # Output: 6