points = []
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
    f.write("Solved in: " + str(i) + "\n")
    for i in range(len(text)):
      if len(set(text[i])) > 1:
        f.write(''.join(text[i]) + "\n")
    f.write('\n\n\n\n\n\n\n\n\n')




