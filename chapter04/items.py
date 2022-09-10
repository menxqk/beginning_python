d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())

it = d.items()
print(len(it))
print(('spam', 0) in it)
print()

d['spam'] = 1
print(d)
print(('spam', 0) in it)
d['spam'] = 0
print(('spam', 0) in it)
print()

print(d.keys())
print()

print(d)
print('pop:', d.pop('url'))
print(d)
print('popitem:', d.popitem())
print(d)
print()

d.setdefault('name', 'N/A')
print(d)
d['name'] = 'Gumby'
d.setdefault('name', 'N/A')
print(d)
d = {}
print(d.setdefault('name'))
print(d)
print()

d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
x = {'title': 'Python Language Website'}
d.update(x)
print(d)
print()

print(d.values())
