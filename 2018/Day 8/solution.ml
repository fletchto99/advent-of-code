type node = {
  children : node list;
  metadata : int list;
  };;

let rec parse_metadata = function
  | 0 -> []
  | n -> try let a = Scanf.scanf " %d" (fun x -> x) in
      a :: (parse_metadata (n-1))
    with e -> Printf.printf "failed to parse metadata"; raise e;;

let rec parse_node =  function
  |0 -> []
  |n -> try let nbChildren, nbMetadata = Scanf.scanf " %d %d" (fun x y -> (x,y)) in
      let children = parse_node nbChildren in
      let meta = parse_metadata nbMetadata in
      {children = children; metadata = meta} :: (parse_node (n-1))
  with e -> Printf.printf "failed to parse node"; raise e;;

let rec sum_metadata = function
  |[] -> 0
  | a::r -> (List.fold_left (+) 0 a.metadata) + (sum_metadata a.children) + (sum_metadata r);;

let rec value_node = function
  | n when (List.length n.children) == 0 -> List.fold_left (+) 0 n.metadata
  | n ->
    List.fold_left (fun old id -> old + (if id <= (List.length n.children) then (value_node (List.nth n.children (id - 1))) else 0)) 0 n.metadata;;

let nodes = parse_node 1;;

Printf.printf "meta sum = %d\n" (sum_metadata nodes);;
