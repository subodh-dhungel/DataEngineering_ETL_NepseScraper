import re

text = '''/* this is a
multiline comment */
Some other text
/* another multiline
comment */'''

pattern = r'/\*.*?\*/'
matches = re.findall(pattern, text, re.DOTALL)
print(matches)
