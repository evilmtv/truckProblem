# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:14:19 2018
@author: Lim Jun Hao
Python 3.6
"""
print ('\n')

from datetime import datetime
import time
import random

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

# Print current time on computer
print (str(datetime.now()), '\n')
# Implement simple timer
current_milli_time = lambda: int(round(time.time() * 1000)) 
startTime = current_milli_time()

# Variable Declarations
currentPosition = 0
fuelOnHand = 0
fuelTaken = 0
fuelUsed = 0
tryCount = 0 # Furthest checked location
n = random.randint(1, 10)
print ('Distance to destination =', n, '\n')
steps = 0
state = 'exploring'
fuelMap = zerolistmaker(2) # Taking fuelMap[0] as start point, fuelMap[1] as position 1 etc..


def geometricSum():
    geoN = tryCount - currentPosition
    if ((tryCount - currentPosition) == 0):
        return 3
    else:
        ratio = 3
        start = 4
        progression = [start * ratio**i for i in range(geoN)]
        return(3 + sum(progression))

def takeFuel(qty):
    global fuelOnHand
    global fuelMap
    global steps
    global fuelTaken
    if (currentPosition > 0):
        if (fuelMap[currentPosition] >= qty):
            fuelMap[currentPosition] -= qty
            fuelOnHand += qty
            steps += 1
    elif (currentPosition == 0):
        fuelOnHand += qty
        fuelTaken += qty
    else:
        print ('\nERROR at takeFuel\n')
    print (fuelMap)
    print('Fuel:', fuelOnHand, '| Position:', currentPosition, '| Task: Refueling', '| Steps:', steps, '| State:', state)
          
def moveAndDrop(direction):
    global fuelOnHand
    global fuelTaken
    global fuelUsed
    global steps
    global currentPosition
    
    if (direction == 'back'):
        currentPosition -= 1
    elif (direction == 'forward'):
        currentPosition += 1

    fuelOnHand -= 1
    fuelUsed += 1
    if (currentPosition == 0):
        fuelTaken -= fuelOnHand
    else:
        fuelMap[currentPosition] += fuelOnHand
    fuelOnHand = 0
    steps += 1
    print (fuelMap)
    print('Fuel:', fuelOnHand, '| Position:', currentPosition, '| Task: Moving', direction, '| Steps:', steps, '| State:', state)

def carryFromPrevious():
    global currentPosition
    global fuelOnHand
    global fuelTaken
    global fuelUsed
    global steps
    global fuelMap
    
    tempGeometricSum = geometricSum()
    
    while (fuelMap[currentPosition] < tempGeometricSum):
        # Fill up truck
        takeFuel(1)
        # Move truck backwards and drop fuel
        moveAndDrop('back')
        # Fill up truck
        takeFuel(3)
        # Move truck forward and drop fuel
        moveAndDrop('forward')
    
    if (currentPosition == tryCount):
        return()
        
    else:
        # Fill up truck
        takeFuel(3)
        # Move truck forward and drop fuel
        moveAndDrop('forward')
        
        carryFromPrevious()
        return()
        

# Main Code
print ('BEGIN \n')
      
# Attempt 'if n = 1'
# Fill up truck
takeFuel(2)
# Move truck forward and drop fuel
moveAndDrop('forward')
# Check if destination reached
if (currentPosition == n):
    state = 'end'
else:
    state = 'returning'
    # Update map
    fuelMap.extend(zerolistmaker(1))
    # Update latest checked distance
    tryCount = 1

while (state != 'end'):
    
    while (state == 'returning'):
        # Fill up truck
        takeFuel(fuelMap[currentPosition])
        # Move truck
        moveAndDrop('back')
        
        if (currentPosition == 0):
            state = 'exploring'
        
    while (state == 'exploring'):
        
        if (currentPosition == 0):
            # Fill up truck
            takeFuel(3)
             #Move truck forward and drop fuel
            moveAndDrop('forward')
            carryFromPrevious()

        if (currentPosition == (tryCount + 1)):
            tryCount += 1
            
            if (currentPosition == n):
                state = 'end'
                
            else:
                # Update map
                fuelMap.extend(zerolistmaker(1))
                print ('\nDestination not reached, insufficient fuel to progress, returning to base\n')
                state = 'returning'
                
        elif (currentPosition == tryCount):
            # Fill up truck
            takeFuel(2)
            # Move truck forward and drop fuel
            moveAndDrop('forward')

print ('\nCurrent Position is at destination, Mission Complete!\n')

print ('Mission took', (current_milli_time() - startTime), 'ms\n')

print ('::Results::')
print ('Fuel taken from start:', fuelTaken)
print ('Fuel actually used:', fuelUsed)
