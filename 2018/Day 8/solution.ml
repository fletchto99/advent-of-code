#load "str.cma"

type node = {
  sum : int ;
  add : int
};;

let parse_tree remaining =
  let counter = ref 0 in

  let get_and_increment ctr =
    let result = !ctr in
    incr ctr;
    result in

  let rec parse (l : int list) : int =
    let rec parse_children (i : int) (j : int) (c : int list) : int list =
      if i < j then parse_children (i + 1) j (c@[parse l])
      else c in

    let rec parse_metadata (i : int) (j : int) (m : int list) : int list =
      if i < j then parse_metadata (i + 1) j m@[int_of_string (List.nth remaining (get_and_increment counter))]
      else m in

    let rec children_metadata_sum i c sum =
      if i < 0 then sum
      else children_metadata_sum (i - 1) c (sum + (List.nth c i)) in

    let node_len = int_of_string (List.nth remaining (get_and_increment counter)) in
    let metadata_len = int_of_string (List.nth remaining (get_and_increment counter)) in
    let children = parse_children 0 node_len [] in
    let metadata = parse_metadata 0 metadata_len [] in
    let metadata_sum = List.fold_left (+) 0 metadata in

    metadata_sum + (children_metadata_sum ((List.length children) - 1) children 0) in
  parse []
;;

let in_ch = open_in "input.txt" in
let line = try input_line in_ch with End_of_file -> exit 0 in
let split = Str.split (Str.regexp "[ \n\r\x0c\t]+") line in
print_int(parse_tree(split));
