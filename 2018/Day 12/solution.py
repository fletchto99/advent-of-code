current = None
nextGen = []
rules = []
iterations = 500
sums = []

for line in open("input.txt"):
    if current is None:
        current = ['.', '.', '.', '.', '.'] + \
            list(line[15:].strip()) + ['.', '.', '.', '.', '.']

    else:
        split = line.split(" ")
        if len(split) == 3:
            rules.append({
                'match': list(split[0].strip()),
                'outcome': split[2].strip()
            })

for i in range(iterations):
    for j in range(2, len(current) - 2):
        found = False
        for rule in rules:
            if current[j - 2] == rule['match'][0] and\
                    current[j - 1] == rule['match'][1] and\
                    current[j] == rule['match'][2] and\
                    current[j + 1] == rule['match'][3] and\
                    current[j + 2] == rule['match'][4]:
                nextGen.append(rule['outcome'])
                found = True
                break
        if not found:
            nextGen.append('.')
    nextGen = nextGen + ['.', '.']
    current = ['.', '.'] + nextGen[:] + ['.', '.']
    nextGen = ['.', '.']
    sums.append(sum([idx - ((i + 1) * 2 + 3)
                     for idx, plant in enumerate(current) if plant == "#"]))

print(sums[19])
print(str(((50000000000 * (sums[499] - sums[498])) -
           ((sums[499] - sums[498]) * 500)) + sums[499]))
