line = []

def parse_node():
  node_len = int(line.pop(0))
  metadata_len = int(line.pop(0))
  node = {
    'children': [parse_node() for i in range(node_len)],
    'metadatas': [int(line.pop(0)) for i in range(metadata_len)]
  }
  return node

def recursive_sum(node, total):
  if node['children']:
    return sum(node['metadatas']) + sum(recursive_sum(child, total) for child in node['children'])
  return sum(node['metadatas'])

def recursive_add(node, total):
  if len(node['children']) == 0:
    return sum(node['metadatas'])
  return sum(recursive_add(node['children'][i-1], total) for i in node['metadatas'] if i-1 < len(node['children']))

with open('input.txt') as f:
  line = f.read().rstrip().split(" ")

root = parse_node()
print(recursive_sum(root, 0))
print(recursive_add(root, 0))
