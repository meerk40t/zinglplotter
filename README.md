# zinglplotter
Zingl-Bresenham plotting algorithms.

The Zingl-Bresenham plotting algorithms are from Alois Zingl's "The Beauty of Bresenham's Algorithm" ( http://members.chello.at/easyfilter/bresenham.html ). They are all MIT Licensed and this library is also MIT licensed. In the case of Zingl's work this isn't explicit from his website, however from personal correspondence "'Free and open source' means you can do anything with it like the MIT licence[sic]."

While the core functions do not require `svgelements`, the initial usage divides this from the svgelements functionality and maintaining that functionality in the process requires it plot the correct elements without issue. So this coupling will be maintained initially with some intent to remove it in the future. 
