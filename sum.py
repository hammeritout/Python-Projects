def sum(lower,upper):
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result
