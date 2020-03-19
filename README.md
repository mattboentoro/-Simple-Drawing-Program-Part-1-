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

### Picture Elements

Create picture elements using the commands below.
```
(line X0 Y0 X1 Y1)
```
Draw a line with one endpoint at (X0, Y0) and the second endpoint at (X1, Y1).
```
(rect X Y W H)
```
Draw an outline of a rectangle whose lower left corner is at (X,Y), and which has a width of W and height
of H. The rectangle should be drawn counter-clockwise starting from the lower left corner.

### Transformation Elements

Create transformations using the commands below.
```
(translate X Y)
```
Translate the following picture element by X units along the x-axis, and Y units along the y-axis.
```
(rotate X)
```
Rotate the following picture element by X degrees about the origin.

### Drawing Parameters

Create drawing parameters using the commands below.
```
(color R G B)
```
Set the current color to (R,G,B). The arguments must be numbers between 0 and 1, inclusive. Initially, R =
G = B = 0 (i.e. black).
```
(linewidth W)
```
Set the current line width to W, which must be a non-negative number. This meaning of this width value is
as that of PostScript, meaning you can pass this value directly to PostScript commands. The initial value
of the line width is 1.

## Input Examples

Zero or more whitespaces are allowed between a parenthesis and the start or end of a command, and between
commands. At least one character of whitespace is required to separate arguments within a command.

For example, the following would draw a thick blue square, rotated 45 degrees.

```
(linewidth 5)
(color 0 0 1)
(rotate 45)(rect 100 100 100 100)
```

## PostScript
The output of your program will be a PostScript document. You can view a PostScript file with any PostScript
viewer. A popular one is gv available on Linux. A PostScript file has the following form:
```
%!PS-Adobe-3.1
commands
showpage
```
The commands of the PostScript language are in postfix notation. The actual PostScript language is free form,
meaning operands and operators can be separated by arbitrary whitespace. Your output, however, must mimic
the reference program to make your program easier to debug and grade. Each command will start on a newline
with operands separated by a single space.

The origin of a PostScript starts at (0,0) in the lower left corner, with x-coordinates increasing to the right and ycoordinates
increasing to the top. To draw something, one builds a path, and then strokes it. The PostScript
interpreter maintains a graphics state, which for our purposes consists of

⋅⋅* A current point, (x,y) coordinate, which is initially undefined.
⋅⋅* A current path.
⋅⋅* A current color, a 3-tuple (r,g,b), where each color intensity r,g,b is between 0 and 1 inclusive. (0,0,0) is
black and (1,1,1) is white.
⋅⋅* A current line thickness, which indicates the thickness of lines drawn when stroking.
