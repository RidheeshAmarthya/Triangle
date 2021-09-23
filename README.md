# Triangle

This program is has five major functions which are explained below:
  1. translate(): Takes a vertex array pointer and (x,y) translate factors. It translates the vertex array points.
  2. scale(): Same as translate but scales the object by multiplying the scale factor with coordinate points.
  3. rotate(): Rotates the points along one of the lines, there is a bug which might cause it to shrink because of a rounding error
  4. draw(): takes the vertex array and draws the shape 
  5. main(): Function with the game loop
 
 PyGame is used only to draw the window and take inputs
 PyOpenGL is used to draw the lines from the GPU
 
Inside the main gameloop are all the function calls. 

vertices_2d and edges_2d are the arrays which store vertex and array data

This program only works with 2D triangles for now.
