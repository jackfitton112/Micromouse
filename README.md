# Stage 2 Project: Micro maze mouse!

## useful links

- https://github.com/joshuaccl/Micromouse
- https://thepihut.com/products/laser-sensor?variant=39710249648323&currency=GBP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=Cj0KCQjwzLCVBhD3ARIsAPKYTcSoC4onmG1kZd8xWm8vhje6eFd_k_qnRxfLlpBjyOzi3iM0Z-LcX0EaArJ3EALw_wcB



## Plan (suedo ish)

- 1 BM = 1 robot width move (TBD depending on size)

- set deg (0 degrees) used to stop the robot going back in its self
- need to def a var (array/list) to track movements to map full maze
```
deg = 0
route = []

if deg == 360:
  deg = 0


if deg != 180 (going back on itself):

  if bot can move 1 BM forward:
      move 1BM forward
      route[] = FD

  else:
    turn right 90 degrees
    deg += 90
    route[] = R90

else:
  turn right 90 degrees
  deg += 90
  route[] = R90

  ```

  this will be used to map out the maze


## Update!

Program tracer now works, a list is passed as the following

`list = ["XXF","R","XXF","L"]`

- XX = int (number of steps)
- F = forward
- R = right 90 degrees
- L - left 90 degrees 
