let rec parse_node(remaining):
  node_len = int(remaining.pop(0))
  metadata_len = int(remaining.pop(0))
  children = [parse_node(remaining) for i in range(node_len)]
  metadata = [int(remaining.pop(0)) for i in range(metadata_len)]
  return {
    'sum': sum(metadata) + (sum(c['sum'] for c in children) if children else 0),
    'add': sum(metadata) if len(children) == 0 else sum(children[i-1]['add'] for i in metadata if i-1 < len(children))
  }


let file = "input.txt"

let () =
     let ic = open_in file in
     let rec build_list infile =
          try
               let line = input_line infile in
               line :: build_list(infile)
          with End_of_file ->
               close_in infile;
               [] in
     let rec print_list = function
          [] -> ()
          | e::l -> print_string e ; print_string " " ; print_list l in
     print_list(build_list(ic))
  print(root['sum'])
  print(root['add'])
