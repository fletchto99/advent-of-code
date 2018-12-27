valid_instructions = [
    {
        'name':
        'addr',
        'operation':
        lambda registers, params: registers[params[0]] + registers[params[1]]
    },
    {
        'name': 'addi',
        'operation': lambda registers, params: registers[params[0]] + params[1]
    },
    {
        'name':
        'mulr',
        'operation':
        lambda registers, params: registers[params[0]] * registers[params[1]],
    },
    {
        'name': 'muli',
        'operation':
        lambda registers, params: registers[params[0]] * params[1],
    },
    {
        'name':
        'banr',
        'operation':
        lambda registers, params: registers[params[0]] & registers[params[1]],
    },
    {
        'name': 'bani',
        'operation':
        lambda registers, params: registers[params[0]] & params[1],
    },
    {
        'name':
        'borr',
        'operation':
        lambda registers, params: registers[params[0]] | registers[params[1]],
    },
    {
        'name': 'bori',
        'operation':
        lambda registers, params: registers[params[0]] | params[1],
    },
    {
        'name': 'setr',
        'operation': lambda registers, params: registers[params[0]],
    }, {
        'name': 'seti',
        'operation': lambda registers, params: params[0],
    },
    {
        'name':
        'gtir',
        'operation':
        lambda registers, params: 1 if params[0] > registers[params[1]] else 0,
    },
    {
        'name':
        'gtri',
        'operation':
        lambda registers, params: 1 if registers[params[0]] > params[1] else 0,
    },
    {
        'name':
        'gtrr',
        'operation':
        lambda registers, params:
            1 if registers[params[0]] > registers[params[1]] else 0
    },
    {
        'name':
        'eqir',
        'operation':
        lambda registers, params: 1 if params[0] == registers[params[1]] else 0
    },
    {
        'name':
        'eqri',
        'operation':
        lambda registers, params: 1 if registers[params[0]] == params[1] else 0
    },
    {
        'name':
        'eqrr',
        'operation':
        lambda registers, params:
            1 if registers[params[0]] == registers[params[1]] else 0
    }
]

ip = -1
program = []

for line in open("input.txt"):
    line = line.rstrip()
    if line.startswith("#"):
        ip = int(line[4])
    else:
        asm = line.split(" ")
        program.append({
            'instruction': asm[0],
            'params': [int(x) for x in asm[1:]]
        })

for i in range(2):
    registers = [i, 0, 0, 0, 0, 0]
    stop = 0
    while registers[ip] < len(program) and stop < 1000:
        stop += 1
        line = program[registers[ip]]
        instruction = list(
            filter(lambda instr: instr['name'] == line['instruction'],
                   valid_instructions))[0]
        registers[line['params'][2]] = instruction['operation'](
            registers, line['params'])
        registers[ip] += 1

    total = 0
    for i in range(1, registers[3] + 1):
        if registers[3] % i == 0:
            total += i
    print(total)
