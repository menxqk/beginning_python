import random

seq = [1,2,3,4,5,6,7,8,9]

print(random.random())
print(random.getrandbits(10))
print(random.uniform(1, 10))
print(random.randrange(1, 10, 2))
print(random.choice(seq))
random.shuffle(seq); print(seq)
print(random.sample(seq, 3))
