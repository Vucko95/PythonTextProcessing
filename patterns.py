import re

text = 'This is a test monkey_@gmail.com another test dog@gmail.com sure!'

# pattern = re.compile("[a-z]+@[a-z]+.[a-z]+")
# Cannot work with Underscores

# 1st one means match any simbol or any letter but not space
pattern = re.compile("[^ ]+@[a-z]+.[a-z]+")

matches = pattern.findall(text)
print(matches)
for match in matches:
    string_match = ''.join(match)
    print(string_match)
