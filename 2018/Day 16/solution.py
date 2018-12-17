valid_instructions = [
  {
    'name': 'addr',
    'operation': lambda registers, params: registers[params[0]] + registers[params[1]],
    'potential_opcodes': set()
  },
  {
    'name': 'addi',
    'operation': lambda registers, params: registers[params[0]] + params[1],
    'potential_opcodes': set(),
  },
  {
    'name': 'mulr',
    'operation': lambda registers, params: registers[params[0]] * registers[params[1]],
    'potential_opcodes': set()
  },
  {
    'name': 'muli',
    'operation': lambda registers, params: registers[params[0]] * params[1],
    'potential_opcodes': set(),
  },
  {
    'name': 'banr',
    'operation': lambda registers, params: registers[params[0]] & registers[params[1]],
    'potential_opcodes': set()
  },
  {
    'name': 'bani',
    'operation': lambda registers, params: registers[params[0]] & params[1],
    'potential_opcodes': set(),
  },
  {
    'name': 'borr',
    'operation': lambda registers, params: registers[params[0]] | registers[params[1]],
    'potential_opcodes': set()
  },
  {
    'name': 'bori',
    'operation': lambda registers, params: registers[params[0]] | params[1],
    'potential_opcodes': set(),
  },
  {
    'name': 'setr',
    'operation': lambda registers, params: registers[params[0]],
    'potential_opcodes': set()
  },
  {
    'name': 'seti',
    'operation': lambda registers, params: params[0],
    'potential_opcodes': set(),
  },
  {
    'name': 'gtir',
    'operation': lambda registers, params: 1 if params[0] > registers[params[1]] else 0,
    'potential_opcodes': set()
  },
  {
    'name': 'gtri',
    'operation': lambda registers, params: 1 if registers[params[0]] > params[1] else 0,
    'potential_opcodes': set(),
  },
  {
    'name': 'gtrr',
    'operation': lambda registers ,params: 1 if registers[params[0]] > registers[params[1]] else 0,
    'potential_opcodes': set(),
  },
  {
    'name': 'eqir',
    'operation': lambda registers,params: 1 if params[0] == registers[params[1]] else 0,
    'potential_opcodes': set()
  },
  {
    'name': 'eqri',
    'operation': lambda registers,params: 1 if registers[params[0]] == params[1] else 0,
    'potential_opcodes': set(),
  },
  {
    'name': 'eqrr',
    'operation': lambda registers,params: 1 if registers[params[0]] == registers[params[1]] else 0,
    'potential_opcodes': set(),
  }
]

samples = []

parsing_line = False
instruction_sample = {
  'possible': set()
}
program = []
for line in open("input.txt"):
  if line == "\n":
    continue
  line = line.rstrip()
  if line.startswith("Before:") or line.startswith("After:"):
    # Since we know a before is always followed by an after
    # we can just assume the next flip is caused by the after
    parsing_line = not parsing_line
    registers = [int(x) for x in line[9:-1].split(", ")]

    if not parsing_line:
      # We've built out the instruction, append it
      instruction_sample['output'] = registers
      samples.append(instruction_sample)
      instruction_sample = {
        'possible': set()
      }
    else:
      instruction_sample['input'] = registers
    continue

  machine_code = [int(x) for x in line.split(" ")]
  if parsing_line:
    instruction_sample['opcode'] = machine_code[0]
    instruction_sample['params'] = machine_code[1:]
  else:
    program.append({
      'opcode': machine_code[0],
      'params': machine_code[1:]
    })

for test in samples:
  for instruction in valid_instructions:
    result = test['input'][:]
    result[test['params'][2]] = instruction['operation'](result, test['params'])
    if result == test['output']:
      instruction['potential_opcodes'].add(test['opcode'])
      test['possible'].add(instruction['name'])

print(len([sample for sample in samples if len(sample['possible']) >= 3]))

# Oof there's gotta be a better way to do this using set differences or something
while len([x for x in valid_instructions if len(x['potential_opcodes']) > 0]):
  for instruction in valid_instructions:
    if len(instruction['potential_opcodes']) == 1:
      instruction['opcode'] = min(instruction['potential_opcodes'])
      for instruction2 in valid_instructions:
        if instruction['opcode'] in instruction2['potential_opcodes']:
          instruction2['potential_opcodes'].remove(instruction['opcode'])

valid_instructions = sorted(valid_instructions, key=lambda x: (x['opcode']))

registers = [0, 0, 0, 0]
for line in program:
  instruction = list(filter(lambda instr: instr['opcode'] == line['opcode'], valid_instructions))[0]
  registers[line['params'][2]] = instruction['operation'](registers, line['params'])
print(registers[0])
