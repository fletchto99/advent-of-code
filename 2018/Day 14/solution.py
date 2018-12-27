scores = [3, 7]
elves = [0, 1]
max_score = 0
max_score_check = []

with open('input.txt') as f:
    score = f.read().rstrip()
    max_score = int(score)
    max_score_check = [int(x) for x in score]

chk1 = False
chk2 = False
i = 0
while True:
    i += 1
    next_score = sum([scores[x] for x in elves])
    scores += [int(x) for x in str(next_score)]
    taken = []

    if chk1 and chk2:
        break

    if not chk1 and i > max_score + 10:
        chk1 = ''.join([str(x) for x in scores[max_score:max_score + 10]])

    if not chk2 and len(scores) >= len(max_score_check):
        offset = min(10, len(scores) - len(max_score_check))
        sub = scores[len(scores) - len(max_score_check) - offset:]
        for i in range(0, len(sub) - len(max_score_check)):
            if sub[i:i + len(max_score_check)] == max_score_check:
                chk2 = len(scores) - len(max_score_check) - offset + i

    for idx, elf in enumerate(elves):
        recipe = (elf + (scores[elf] + 1)) % len(scores)
        while recipe in taken:
            recipe = (recipe + 1) % len(scores)
        elves[idx] = recipe
        taken.append(recipe)

print(chk1)
print(chk2)
