import re

text = 'Computer says "no." Phone says "yes."'
pattern = r'"(.*?)"'

matches = re.findall(pattern, text)
print(matches)
