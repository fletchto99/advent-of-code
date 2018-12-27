def parse_node(remaining):
    node_len = int(remaining.pop(0))
    metadata_len = int(remaining.pop(0))
    children = [parse_node(remaining) for i in range(node_len)]
    metadata = [int(remaining.pop(0)) for i in range(metadata_len)]
    return {
        'sum':
        sum(metadata) + (sum(c['sum'] for c in children) if children else 0),
        'add':
        sum(metadata) if len(children) == 0 else sum(
            children[i - 1]['add'] for i in metadata if i - 1 < len(children))
    }


with open('input.txt') as f:
    root = parse_node(f.read().rstrip().split(" "))
    print(root['sum'])
    print(root['add'])
