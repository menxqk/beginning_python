with open('otherfile.txt') as f:
    char = f.read(1)
    while char:
        print(char, end='')
        char = f.read(1)
print()
print()

import fileinput
for line in fileinput.input('otherfile.txt'):
    print(line, end='')
print()