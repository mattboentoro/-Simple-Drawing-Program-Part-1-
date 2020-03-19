# "Simple" Drawing Program Part 1

Create a simple drawing program.

A picture is worth a thousand words. In this assignment, transform those words back into a picture. You'll
translate a drawing description into a PostScript file that will produce the specified picture. Your program should
read input from stdin and output the PostScript file to stdout.

## Input Language

A drawing consists of zero or more picture elements, with each element modified by zero or more
transformations. The drawing may also have zero or more parameter settings before any picture element. All
numbers should be handled in floating-point. The coordinate (0,0) is the origin and is the lower left corner of the
drawing. X-coordinate values increase to the right and y-coordinate values increase to the top.

Create picture elements using the commands below.
