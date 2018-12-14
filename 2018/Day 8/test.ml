let counter = ref 0;;
let get_and_increment ctr =
  let result = !ctr in
  incr ctr;
  result
;;

let () =
  print_int(get_and_increment(counter));
  print_int(get_and_increment(counter));
  print_int(get_and_increment(counter));
  print_int(get_and_increment(counter));
