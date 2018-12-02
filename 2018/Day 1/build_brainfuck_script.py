# I got lazy and didn't feel like reading signed integers > 1 byte
# in brainfuck, so this script processes it for me :D
# I could only read so many >>.<<.<[][ before my brain was mush

to_write = []

with open('input.txt', 'r') as template:
    lines = template.readlines()

    for line in lines:
      add = False
      # ensure we start building the number in the next 32-bit cell
      to_append = ">"

      # We generate the powerseries to store the number. We must track
      # which cell we're in (left or right). If we finish in the right
      # cell then the number must be shifted back to the left. This
      # enables us to use quite a few less characters to generate large
      # numbers (up to MAX_INTEGER)
      left = True
      for idx,char in enumerate(line.strip()):
        # check if we're adding or subtracting
        if idx == 0:
          add = char == "+"
        else:
          if idx == len(line) - 2:
            # 1's column, increment the cell value by n
            to_append += '+' * int(char)
          else:
            # nth column greater than 1, increment the cell value by n
            to_append += '+' * int(char)
            # To generate the power series of the number we use 2 cells
            # constantly multiplying the value by 10 (to represent the
            # number in base 10 easily)
            if left:
              to_append += '[>++++++++++<-]>'
            else:
              to_append += '[<++++++++++>-]<'
            left = not left
      # If the number was greater than 9 (I.E. used powerseries generator)
      # we need to determine where the result ended up. If the result was
      # in the left cell, there's no need to shift it since it's in the
      # desired location. However if it's in the right cell then we must
      # shift it back. E.G result is 2, [1][0][2] should be [1][2][0] for
      # simple addition. To shift it we decrement the right cell and
      # increment the left cell, until the right cell is 0
      if abs(int(line)) > 9 and not left:
        to_append += '[-<+>]<'
      to_write.append(to_append)
      if add:
        # ADD [A]+[B] (cells in that order), [A]->[B]
        # If we're performing an add we move the contents of the left
        # cell into the right cell by decrementing the left cell by 1
        # and incrementing the right cell by 1 until the left side is
        # 0 we then move back into the current cell
        to_write.append('<[->+<]>')
      else:
        # SUB [A]-[B] (cells in that order), [A]<-[B]
        # If we're subtracting we subtract one from the left cell and
        # then one from the right cell. Unfortunately that leaves the
        # result in the left cell, which isn't desirable so now have
        # to shift the contents of the left cell back into the right
        # This is done by subtracting 1 from the left cell and adding
        # 1 to the right cell until the left cell is empty, finally
        # moving the pointer back to the right cell
        to_write.append('[<->-]<[->+<]>')

# We write the result to a file called out.txt, however the contents of
# out.txt should replace the arithmetic section of `sample.bf` in order
# to build the solution for part1 :)
with open("out.txt","w+") as out:
  for line in to_write:
    out.write(line+'\n')

