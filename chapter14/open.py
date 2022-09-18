from urllib.request import urlopen
webpage = urlopen('http://www.python.org')

import re
text = webpage.read()
m = re.search(b'<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
print(m.group(1).decode())