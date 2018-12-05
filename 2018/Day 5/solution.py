import operator

results = []
to_replace = []
alphabet = list('abcdefghijklmnopqrstuvwxyz')

for char in alphabet:
  to_replace.append(char.upper()+char)
  to_replace.append(char+char.upper())

def merge(polymer):
  poly = polymer
  length = 0
  while length != len(poly):
    length = len(poly)
    for pair in to_replace:
      poly = poly.replace(pair, "")
  return poly

with open('input.txt') as f:
  line = f.read().rstrip()
  print(len(merge(line)))

  for char in alphabet:
    modified = line
    modified = modified.replace(char, "").replace(char.upper(), "")
    results.append(len(merge(modified)))
  print(min(results))
