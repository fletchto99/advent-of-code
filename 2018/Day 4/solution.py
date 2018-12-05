from datetime import datetime
import operator

actions = []
guards = []
begin = 0
end = 0

for line in open('input.txt'):
  splt = line.split(" ")
  timestamp = str((splt[0])[1:]) + " " + str((splt[1][:-1]))
  parsed_timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
  action = ""
  guard = -1

  if "wakes" in splt[2]:
    action = "wake"
  elif "falls" in splt[2]:
    action = "sleeps"
  else:
    guard = int(str(splt[3])[1:])
    action = "begins" if "begins" in splt[4] else "ends"
    to_add = {'guard': guard, 'sleeping_time': dict((el,0) for el in range(60))}
    if to_add not in guards:
      guards.append(to_add)

  actions.append({'time':timestamp,'action':action,'guard':guard})

actions.sort(key=lambda x:x['time'])

guard = -1
sleep_start = 0

most_asleep = {}

for idx,val in enumerate(actions):
  if val['action'] == "begins":
    guard = val['guard']
  if val['action'] == "ends":
    sleep_start = 0
    guard = -1
  elif val['action'] == "sleeps":
    val['guard'] = guard
    sleep_start = int(val['time'].split(":")[1])
  elif val['action'] == "wake":
    val['guard'] = guard
    time_sleeping = int(val['time'].split(":")[1]) - sleep_start
    sleep_end = int(val['time'].split(":")[1])
    match = next((val for val in guards if val["guard"] == guard), None)
    for i in range(sleep_start, sleep_end):
      match['sleeping_time'][i] += 1
    if guard in most_asleep:
      most_asleep[guard] += time_sleeping
    else:
      most_asleep[guard] = time_sleeping

most = int(max(most_asleep.items(), key=operator.itemgetter(1))[0])
match = next((guard for guard in guards if guard["guard"] == most), None)
res = int(max(match['sleeping_time'].items(), key=operator.itemgetter(1))[0])*most
print(res)

for guard in guards:
  guard['most'] =  max(guard['sleeping_time'].items(), key=operator.itemgetter(1))[0]
  guard['amount'] = guard['sleeping_time'][guard['most']]

guards.sort(key=lambda x:x['amount'], reverse=True)

res = int(guards[0]['most']) * int(guards[0]['guard'])
print(res)
