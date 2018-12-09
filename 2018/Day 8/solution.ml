(* def parse_node(remaining):
  node_len = int(remaining.pop(0))
  metadata_len = int(remaining.pop(0))
  return {
    'children': [parse_node(remaining) for i in range(node_len)],
    'metadatas': [int(remaining.pop(0)) for i in range(metadata_len)]
  } *)

type tree =
  {children:int list; metadata:int list}

let rec parseNode remaining =
  "test";;

let rec sumTree root total =
  "test";;

let rec addTree root total =
  "test";

let () =
  let ic = open_in "input.txt" in
  let line = input_line ic in
  let root = Str.split(Str.regexp(" ")) line in
  print_endline root

