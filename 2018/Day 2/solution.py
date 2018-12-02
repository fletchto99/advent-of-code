with open('input.txt') as fp:
  lines = fp.readlines()

  twos = 0
  threes = 0

  letters = dict()
  found_two = False
  found_three = False

  for line in lines:
    found_two = False
    found_three = False
    for char in line:
      if char in letters:
        letters[char] = letters[char] + 1
      else:
        letters[char] = 1
    for letter in letters:
      print(letters[letter])
      if letters[letter] == 2 and not found_two:
        found_two = True
        twos += 1
      if letters[letter] == 3 and not found_three:
        found_three = True
        threes += 1
    letters = dict()

  print(twos*threes)
