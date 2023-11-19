# zinglplotter
Zingl-Bresenham plotting algorithms.

The Zingl-Bresenham plotting algorithms are from Alois Zingl's "The Beauty of Bresenham's Algorithm" ( http://members.chello.at/easyfilter/bresenham.html ). They are all MIT Licensed and this library is also MIT licensed. In the case of Zingl's work this isn't explicit from his website, however from personal correspondence "'Free and open source' means you can do anything with it like the MIT licence[sic]."

These algorithms are error-carry-forward algorithms such that they use only integer math to plot pixel positions, and curves like quadratic and cubic beziers do not need to be turned into tiny lines or checked for how small a line should be used. They merely travel from one pixel to the next pixel carrying the error forward. 

# Functions

This library is a series of plot line generators converted from C++.

* plot_line(x0, y0, x1, y1)
* plot_quad_bezier_seg(x0, y0, x1, y1, x2, y2)
* plot_quad_bezier(x0, y0, x1, y1, x2, y2)
* plot_cubic_bezier_seg(x0, y0, x1, y1, x2, y2, x3, y3)
* plot_cubic_bezier(x0, y0, x1, y1, x2, y2, x3, y3)
* draw_line_aa(x0, y0, x1, y1)

These do Zingl-Bresenham algorithms for line, quad, cubic. The `_seg` function perform the draw but only for rational segments (no inversion points). The `_aa` function performs the same thing but in an anti-alias manner.

```python
from zinglplotter import plot_line
for x, y in plot_line(0, 0, 5, 8):
    print(f"({x},{y})")
```

Will result in:
``python
(0,0)
(1,1)
(1,2)
(2,3)
(3,4)
(3,5)
(4,6)
(4,7)
(5,8)
``

```python
from zinglplotter import plot_quad_bezier
for x, y in plot_quad_bezier(0, 0, 9, 4, 0, 10):
    print(f"({x},{y})")
```

Will result in:
``
(0,0)
(1,0)
(2,1)
(3,2)
(4,3)
(5,4)
(5,5)
(5,5)
(5,6)
(4,7)
(3,8)
(2,9)
(1,9)
(0,10)
``
