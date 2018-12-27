carts = []
track = []
idx = 0
for index, line in enumerate(open("input.txt")):
    inp = list(line)
    for i in range(len(inp)):
        if inp[i] == "v" or inp[i] == "^":
            carts.append({
                'direction': inp[i],
                'x': i,
                'y': index,
                'intersection': 0,
                'removed': False
            })
            inp[i] = "|"
        elif inp[i] == ">" or inp[i] == "<":
            carts.append({
                'direction': inp[i],
                'x': i,
                'y': index,
                'intersection': 0,
                'removed': False
            })
            inp[i] = "-"
    track.append(inp)

collide = False
while True:
    carts = sorted(carts, key=lambda x: (x['y'], x['x']))
    for cart in carts:
        if not cart['removed']:
            if cart['direction'] == "^":
                cart['y'] -= 1
                track_piece = track[cart['y']][cart['x']]
                if track_piece == "/":
                    cart['direction'] = ">"
                elif track_piece == "\\":
                    cart['direction'] = "<"
                elif track_piece == "+":
                    if cart['intersection'] % 3 == 0:
                        cart['direction'] = "<"
                    elif cart['intersection'] % 3 == 2:
                        cart['direction'] = ">"
                    cart['intersection'] += 1
            elif cart['direction'] == "v":
                cart['y'] += 1
                track_piece = track[cart['y']][cart['x']]
                if track_piece == "/":
                    cart['direction'] = "<"
                elif track_piece == "\\":
                    cart['direction'] = ">"
                elif track_piece == "+":
                    if cart['intersection'] % 3 == 0:
                        cart['direction'] = ">"
                    elif cart['intersection'] % 3 == 2:
                        cart['direction'] = "<"
                    cart['intersection'] += 1
            elif cart['direction'] == ">":
                cart['x'] += 1
                track_piece = track[cart['y']][cart['x']]
                if track_piece == "/":
                    cart['direction'] = "^"
                elif track_piece == "\\":
                    cart['direction'] = "v"
                elif track_piece == "+":
                    if cart['intersection'] % 3 == 0:
                        cart['direction'] = "^"
                    elif cart['intersection'] % 3 == 2:
                        cart['direction'] = "v"
                    cart['intersection'] += 1
            elif cart['direction'] == "<":
                cart['x'] -= 1
                track_piece = track[cart['y']][cart['x']]
                if track_piece == "/":
                    cart['direction'] = "v"
                elif track_piece == "\\":
                    cart['direction'] = "^"
                elif track_piece == "+":
                    if cart['intersection'] % 3 == 0:
                        cart['direction'] = "v"
                    elif cart['intersection'] % 3 == 2:
                        cart['direction'] = "^"
                    cart['intersection'] += 1
            for cart2 in carts:
                if (cart2 != cart and
                        cart2['x'] == cart['x'] and
                        cart2['y'] == cart['y'] and
                        not cart['removed'] and
                        not cart2['removed']):
                    if not collide:
                        print(str(cart['x']) + "," + str(cart['y']))
                        collide = True
                    cart['removed'] = True
                    cart2['removed'] = True
                    break
    filtered = list(filter(lambda x: not x['removed'], carts))
    if len(filtered) == 1:
        print(str(filtered[0]['x']) + "," + str(filtered[0]['y']))
        break
