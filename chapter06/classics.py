def factorial1(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial1(n-1)

print(factorial1(5))
print(factorial2(5))
print()

def power1(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

def power2(x, n):
    if n == 0:
        return 1
    else:
        return x * power2(x, n-1)

print(power1(2, 3))
print(power2(2, 3))
print()

def binary_search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return binary_search(sequence, number, middle + 1, upper)
        else:
            return binary_search(sequence, number, lower, middle)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)
print(binary_search(seq, 34))
print(binary_search(seq, 100))
