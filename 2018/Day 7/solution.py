steps = {}
incomplete = []
completed = []
base_time = 60
max_workers = 5

for line in open('input.txt'):
  split = line.split(" ")
  requires = split[1]
  find = split[7]

  incomplete.append(find)

  if find in steps:
    steps[find]['requires'].append(requires)
  else:
    steps[find] = {
      'requires': [],
      'time': ord(find) - 64 + base_time
    }
    steps[find]['requires'].append(requires)

  if requires not in steps:
    steps[requires] = {
      'requires': [],
      'time': ord(requires) - 64 + base_time
    }

print(steps)

incomp = incomplete.copy()

while True:
  avaliable = []
  for step, data in steps.items():
    if step not in completed:
      good = True
      for requirement in data['requires']:
        if requirement not in completed:
          good = False
      if good:
        avaliable.append(step)
  avaliable.sort()
  completed.append(avaliable[0])
  if avaliable[0] in incomp:
    incomp.remove(avaliable[0])

  if len(completed) == len(steps):
    break

print("".join(str(x) for x in completed))

completed = []
global_time = 0
workers = []
while True:
  avaliable = []

  if len(workers) > 0:
    workers = sorted(workers, key=lambda x: (x[1], x[2], x[0]))
    if workers[0][1] <= 0:
      complete = workers.pop(0)
      completed.append(complete[0])
      if complete[0] in incomplete:
        incomplete.remove(complete[0])

  if len(completed) == len(steps):
    break

  if len(workers) != max_workers:
    for step, data in steps.items():
      if step not in completed:
        good = True
        for requirement in data['requires']:
          if requirement not in completed:
            good = False
        if good:
          free = True
          for worker in workers:
            if worker[0] == step:
              free = False
          if free:
            avaliable.append(step)
  avaliable.sort()
  while len(workers) != max_workers and len(avaliable) > 0:
    add_worker = avaliable.pop(0)
    workers.append([add_worker, steps[add_worker]['time'], global_time])

  global_time += 1
  for worker in workers:
    worker[1] -= 1

print(global_time)
