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
