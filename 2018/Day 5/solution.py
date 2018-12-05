import operator

results = []
to_replace = []
to_replace2 = []
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for char in alphabet:
  to_replace.append(""+char.upper()+char)

for char in alphabet:
  to_replace2.append(""+char+char.upper())

def merge(polymer):
  poly = polymer
  poly2 = ""
  while poly != poly2:
    poly2 = poly
    for pair in to_replace:
      poly = poly.replace(pair, "")
    for pair in to_replace2:
      poly = poly.replace(pair, "")
  return poly

with open('input.txt') as fp:
  lines = fp.readlines()

  for line in lines:
    print(len(merge(line))-1)

    for char in alphabet:
      modified = line
      modified = modified.replace(char, "")
      modified = modified.replace(char.upper(), "")
      results.append(len(merge(modified))-1)
    print(min(results))







