from multiprocessing import Pool, TimeoutError

size = 300
serial_no = None

with open('input.txt') as f:
  serial_no = int(f.read().rstrip())

grid = [[int(str((((x+11)*(y+1))+serial_no)*(x+11))[-3])-5 for y in range(size)] for x in range(size)]

def compute_best(data):
  x = data['x']
  y = data['y']
  best_x = 0
  best_y = 0
  best_size = 0
  best_area = 0

  best_x_3 = 0
  best_y_3 = 0
  best_area_3 = 0

  to = min(300-x,300-y)
  area = grid[x][y]

  for s in range(1, to):
    if best_area == None or area > best_area:
      best_x = x+1
      best_y = y+1
      best_size = s
      best_area = area
    if s == 3 and (best_area_3 == None or area > best_area_3):
      best_area_3 = area
      best_x_3 = x+1
      best_y_3 = y+1
    for u in range(s+1):
      area += grid[x+u][y+s]
      area += grid[x+s][y+u]
    area -= grid[x+s][y+s]

  return {
    'best_x': best_x,
    'best_y': best_y,
    'best_area': best_area,
    'best_size': best_size,
    'best_x_3': best_x_3,
    'best_y_3': best_y_3,
    'best_area_3': best_area_3
  }

data = []
for x in range(size):
  for y in range(size):
    data.append({'x': x, 'y': y})
results = Pool(20).map(compute_best, data)

res_3 = sorted(results, key = lambda x : x['best_area_3'], reverse=True)
print(res_3[0]['best_x_3'])
print(res_3[0]['best_y_3'])

res = sorted(results, key = lambda x : x['best_area'], reverse=True)
print(res[0]['best_x'])
print(res[0]['best_y'])
print(res[0]['best_size'])
