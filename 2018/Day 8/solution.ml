#load "str.cma"

(* Currently unused, will store node information *)
type node ={ sum : int ; add : int };;

(* Parses the root node in the tree *)
let parse_tree remaining =
  (*
   * A global counter to store the index we're at
   * Unlike my python implementation I can't just
   * pop from the front of the list since OCaml
   * lists are immutable
   *)
  let counter = ref 0 in

  (* Essentially like doing ++crt *)
  let get_and_increment ctr =
    let result = !ctr in
    incr ctr;
    result in

  (*
   * The main node parsing function which works by
   * determining how many children nodes we should
   * parse followed by paring the children nodes.
   * Next we parse the metadata and store them in
   * a list for later use. Finally we sum the metadata
   * along with the sum of all of the children's
   * metadata
   *
   * l: The flat tree as a list of ints
   *)
  let rec parse l =
    (*
     * This recursive function parses all of the children
     * nodes for a given node. We go from left -> right
     * along the flat tree (list) to parse the children
     * a recursive call to parse is made which parses
     * the child node, with the final results being
     * stored in the list c
     *
     * i: How many nodes have been processed
     * j: How many nodes we need to process
     * c: The list to store the children nodes in
     *)
    let rec parse_children i j c =
      if i < j then parse_children((i + 1) j (c :: parse(l)))
      else c in

    (*
     * Similar to parse_children, this parses the
     * metadatas for the given node. Unlike parse_children,
     * we make no recursive call to the parent parse function
     *
     * i: How many list items have been processed
     * j: The total amount of list items to process
     * m: A list of ints which represent the metadata
     *)
    let rec parse_metadata i j m =
      if i < j then parse_metadata (i + 1) j (m :: List.nth(remaining get_and_increment(counter)))
      else m in

    (*
     * This computes the sum of all of the children's metadata
     * for any given node (in our case, the root node). Unlike
     * the other functions, which go left -> right, this one
     * goes right -> left (with the 0th index being the last
     * one which needs processing)
     *
     * i: The current index being processed in the children nodes
     * children:
     * c: the children nodes to process
     * sum: The total sum
     *)
    let rec children_metadata_sum i c sum =
      if i < 0 then sum
      else children_metadata_sum (i - 1) (sum + List.nth(c i)) c in

    let node_len = List.nth(remaining get_and_increment(counter)) in
    let metadata_len = List.nth(remaining get_and_increment(counter)) in
    let children = parse_children 0 node_len [] in
    let metadata = parse_metadata 0 metadata_len [] in
    let metadata_sum = List.fold_left (+) 0 in

    (metadata_sum + children_metadata_sum((List.length(children) - 1) children 0)) in
  parse []
;;

(*
 * Converts the input from a list of strings
 * to a list of ints
 *
 * input: a list of strings that are all valid numbers
 *)
let parse_input input =
  (*
   * The main parsing function
   *
   * i: The index we're currently parsing
   * l: the list to prepend the int to
   *
   * Returns l, a list of ints
   *)
  let rec parse i l =
    if i < 0 then l
    else parse (i - 1) (int_of_string (List.nth input i) :: l) in
  parse (List.length(input)-1) []
;;

let () =
  (* Open the file *)
  let in_ch = open_in "input.txt" in

  (* Read the first line into a string *)
  let line = try input_line in_ch with End_of_file -> exit 0 in

  (* Split the string on whitespace and store as a list of ints*)
  let inp = parse_input(Str.split(Str.regexp "[ \n\r\x0c\t]+") line) in

  (* Calculate the sum of the root node *)
  print_int(parse_tree(inp));
