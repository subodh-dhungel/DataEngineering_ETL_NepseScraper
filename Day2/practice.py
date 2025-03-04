import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

emails:
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r"[a-zA-Z0-9_.-+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
