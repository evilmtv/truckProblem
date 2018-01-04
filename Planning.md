Version 1: Simple

variables: position=0, fuel=0, tryCount=0, n=RAND, steps, fuelTaken=0, fuelUsed=0

Assumptions:
  -infinite supply of fuel at start point
  -truck(program) will not 'know' the distance of the endpoint until it reaches it

Theory:
  -truck will attempt to build a sustainable path point by point incrementally by leaving sufficient fuel for a return journey should the latest point not be the end point

Leave one fuel behind at each point before proceeding to next point
It costs three fuel to bring one fuel to the next point and return to the original point: two spent and one left at next point.
  Thus, it costs 9 fuel at a point to end up at next point with 3 fuel and 1 fuel left on the original point for the return trip
    Thus, it requires 0, 1:27fuel to end up with 0, 1:1fuel, 2:1fuel, 3:3fuel to attempt: 0, 1:1fuel, 2:1fuel, 3:1fuel, 4:1fuel(currentPos)
