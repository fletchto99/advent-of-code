with open('input.txt') as fp:
  lines = fp.readlines()

  for line in lines:
    for line2 in lines:
      if line != line2:
        mismatch = 0
        mismatch_idx = 0
        for idx, val in enumerate(line):
          if mismatch > 1:
            break
          if val != line2[idx]:
            mismatch += 1
            mismatch_idx = idx
        if mismatch == 1:
          print(line)
          print(line2)
          print(mismatch_idx)


