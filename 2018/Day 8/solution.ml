#load "str.cma"

type node = {
  sum : int;
  add : int
};;

let parse_tree remaining =
  let counter = ref 0 in

  let get_and_increment ctr =
    let result = !ctr in
    incr ctr;
    result in

  let rec parse l =
    let rec parse_children i j c =
      if i < j then parse_children (i + 1) j (c@[parse l])
      else c in

    let rec parse_metadata i j m =
      if i < j then parse_metadata (i + 1) j m@[int_of_string (List.nth remaining (get_and_increment counter))]
      else m in

    let rec children_metadata_sum i c sum =
      if i < 0 then sum
      else children_metadata_sum (i - 1) c (sum + (List.nth c i).sum) in

    let rec children_metadata_add ms m c i sum =
      if (List.length c) == 0 then ms
      else if i < 0 then sum
      else if (List.nth m i) - 1 < List.length c then children_metadata_add ms m c (i - 1) (sum + (List.nth c ((List.nth m i) -1)).add)
      else children_metadata_add ms m c (i - 1) sum in

    let node_len = int_of_string (List.nth remaining (get_and_increment counter)) in
    let metadata_len = int_of_string (List.nth remaining (get_and_increment counter)) in
    let children = parse_children 0 node_len [] in
    let metadata = parse_metadata 0 metadata_len [] in
    let metadata_sum = List.fold_left (+) 0 metadata in

    {
      sum=metadata_sum + (children_metadata_sum ((List.length children) - 1) children 0);
      add=children_metadata_add metadata_sum metadata children ((List.length metadata) - 1) 0
    } in
  parse []
;;

let in_ch = open_in "input.txt" in
let line = try input_line in_ch with End_of_file -> exit 0 in
let result = parse_tree (Str.split (Str.regexp "[ \n\r\x0c\t]+") line) in
print_int result.sum;
print_endline "";
print_int result.add;
print_endline "";
