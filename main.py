import re

# p=re.compile('[a-z]+')
# p = re.compile('(\d+)([SDT])([*#]?)')
p = re.compile('(\d+)([SDT])([*#]?)')
result = p.findall('a bca abab acb')
print(result)