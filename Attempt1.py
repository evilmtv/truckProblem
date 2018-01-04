# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:14:19 2018
@author: Lim Jun Hao
Python 3.6
"""

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

#Print current time on computer
from datetime import datetime
print (str(datetime.now()))

#Implement simple timer
import time
tfulls = time.time() 

# Variable Declarations
currentPosition = 0
fuelOnHand = 0
fuelTaken = 0
fuelUsed = 0
tryCount = 0 #Furthest checked location
import random
n = 3 #random.randint(1, 10)
print (n)
steps = 0
state = 'exploring'
fuelMap = zerolistmaker(n + 1) #Taking fuelMap[0] as start point, fuelMap[1] as position 1 etc..
#fuelMap.extend(zerolistmaker(5))

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
        print ('ERROR at takeFuel')
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
    
    while (fuelMap[currentPosition] < ((3**(tryCount - currentPosition + 1)) - 0)):
        #Fill up truck
        takeFuel(1)
        #Move truck backwards and drop fuel
        moveAndDrop('back')
        #Fill up truck
        takeFuel(3)
        #Move truck forward and drop fuel
        moveAndDrop('forward')
    
    if (currentPosition == tryCount):
        return()
    else:
        #Fill up truck
        takeFuel(3)
        #Move truck forward and drop fuel
        moveAndDrop('forward')
        
        carryFromPrevious()
        return()


#Main Code

print (fuelMap)
print('#', steps, 'Fuel:', fuelOnHand, 'Position:', currentPosition, 'Task:', state)
      
#Fill up truck
takeFuel(2)
#Move truck forward and drop fuel
moveAndDrop('forward')

tryCount += 1
      
if (currentPosition == n):
    state = 'end'
else:
    state = 'returning'
    tryCount = 1

while (state != 'end'):
    if (state == 'returning'):
        #Fill up truck
        takeFuel(fuelMap[currentPosition])
        
        #Move truck
        moveAndDrop('back')
        if (currentPosition == 0):
            state = 'exploring'
        
    while (state == 'exploring'):
        if (currentPosition == 0):
            #Fill up truck
            takeFuel(3)
            #Move truck forward and drop fuel
            moveAndDrop('forward')
            carryFromPrevious()

        if (currentPosition == (tryCount + 1)):
            tryCount += 1
            if (currentPosition == n):
                state = 'end'
            else:
                state = 'returning'
        elif (currentPosition == tryCount):
            #Fill up truck
            takeFuel(2)
            
            #Move truck forward and drop fuel
            moveAndDrop('forward')

print ('Mission Complete')