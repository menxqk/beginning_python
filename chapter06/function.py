def fibonacci(num):
    'Calculates the fibonacci result for n'
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print(fibonacci(10))
print(fibonacci(15))
