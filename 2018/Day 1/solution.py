# Solve P1 in one linee
# print(sum(int(x) for x in open("input.txt")))

with open('input.txt') as fp:
    lines = fp.readlines()
    frequencies = {0: True}
    frequency = 0
    repeated = None
    printed = False

    while repeated is None:
      for line in lines:
        frequency += int(line)
        if frequency in frequencies and repeated is None:
          repeated = frequency
        frequencies[frequency] = True

      if printed is False:
        print(frequency)
        printed = True

    print(repeated)
