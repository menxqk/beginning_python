lst = [1,2,3]
lst.append(4)
print(lst)

lst.clear()
print(lst)

a = [1,2,3]
b = a.copy()
b[1] = 4
print(a)
print(b)

print(a.count(1))

b = [4,5,6]
a.extend(b)
print(a)

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))
print(knights[4])

numbers = [1,2,3,5,6,7]
numbers.insert(3, 'four')
print(numbers)

x = [1,2,3]
print(x)
print(x.pop())
print(x)
print(x.pop(0))

x = ['to', 'be', 'or', 'not', 'to', 'be']
print(x)
x.remove('be')
print(x)

x.reverse()
print(x)

x.sort()
print(x)

print(sorted('Python'))
