import re

some_text = 'alpha, beta,,,,gamma    delta'
print(re.split('[, ]+', some_text))
print()

pat = '[a-zA-Z]+'
text = '"Hmm... Err -- are you sure?" he said, sounding insecure.'
print(re.findall(pat, text))
print()

pat = r'[.?\-",]+'
print(re.findall(pat, text))
print()

pat = '{name}'
text = 'Dear {name}...'
print(re.sub(pat, 'Mr. Gumby', text))
print()

print(re.escape('www.python.org'))
print(re.escape('But where is the ambiguity'))
