with open('input.txt') as fp:
  lines = fp.readlines()

  twos = 0
  threes = 0
  same = ""

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
      if letters[letter] == 2 and not found_two:
        found_two = True
        twos += 1
      if letters[letter] == 3 and not found_three:
        found_three = True
        threes += 1
    letters = dict()

    if same == "":
      for line2 in lines:
        if line != line2:
          matching = ""
          mismatch = 0
          for idx, val in enumerate(line):
            if mismatch > 1:
              matching = ""
              break
            if val != line2[idx]:
              mismatch += 1
            else:
              matching += val
          if mismatch == 1:
            same = matching

  print(twos*threes)
  print(same)
