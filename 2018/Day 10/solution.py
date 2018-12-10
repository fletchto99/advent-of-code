points = []
potentials = []
size = 350
f = open("output.txt", "w")

for line in open('input.txt'):
  points.append({
    'x': int(line.split("<")[1].split(",")[0].strip()),
    'y': int(line.split("<")[1].split(",")[1].split(">")[0].strip()),
    'x_velocity': int(line.split("<")[2].split(",")[0].strip()),
    'y_velocity': int(line.split("<")[2].split(",")[1].split(">")[0].strip())
  })

for i in range(15000):
  text = [['.' for _ in range(size)] for _ in range(size)]
  skip = False
  for point in points:
    x = point['x'] + i * point['x_velocity']
    y = point['y'] + i * point['y_velocity']
    if x >= 0 and y >= 0 and x < size and y < size:
      text[y][x] = "#"
    else:
      skip = True
  if not skip:
    lines = []
    count = 0
    trim_start = size
    trim_end = 0
    for x in range(len(text)):
      if len(set(text[x])) > 1:
        count += 1
        lines.append(''.join(text[x]))
        if text[x].index("#") < trim_start:
          trim_start = text[x].index("#")
        last_index = len(text[x]) - text[x][::-1].index("#") - 1
        if last_index > trim_end:
          trim_end = last_index
    potentials.append({
      'msg': '\n'.join([line[trim_start:trim_end] for line in lines]),
      'count': count,
      'time': i
    })
  if i % 100 == 0:
    print(str(i) + "/15000")

potentials = sorted(potentials, key=lambda k: k['count'])

print(potentials[0]['msg'])
print('Found at: ' + str(potentials[0]['time']))
