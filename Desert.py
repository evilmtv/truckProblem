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

def zero_list_maker(n):
    listofzeros = [0] * n
    return listofzeros

# Print current time on computer
print (str(datetime.now()), '\n')
# Implement simple timer
current_milli_time = lambda: int(round(time.time() * 1000))
startTime = current_milli_time()

# Variable Declarations
current_position = 0
fuel_on_hand = 0
fuel_taken = 0
fuel_used = 0
try_count = 0 # Furthest checked location
steps = 0
state = 'exploring'
fuel_map = zero_list_maker(2) # Taking fuel_map[0] as start point, fuel_map[1] as position 1 etc..

# Request user for distance
try:
    n = int(input("Distance? ").strip())
except ValueError:
    n = random.randint(1, 10)
print ('Distance to destination =', n, '\n')

# To explore 3 units away from start point, the truck has to first bring 7 units of fuel to 1 unit away from start point
# To explore 4 units away from start point, the truck has to first bring 19 units of fuel to 1 unit away from start point
# The series follows a geometric sum where the nth term can easily be called using this function and n is defined by try_count and current_position
def geometric_sum():
    geoN = try_count - current_position
    if ((try_count - current_position) == 0):
        return 3
    else:
        ratio = 3
        start = 4
        progression = [start * ratio**i for i in range(geoN)]
        return(3 + sum(progression))

def take_fuel(qty):
    global fuel_on_hand
    global fuel_map
    global steps
    global fuel_taken
    if (current_position > 0):
        if (fuel_map[current_position] >= qty):
            fuel_map[current_position] -= qty
            fuel_on_hand += qty
            steps += 1
    elif (current_position == 0):
        fuel_on_hand += qty
        fuel_taken += qty
    else:
        print ('\nERROR at take_fuel\n')
    print (fuel_map)
    print('Fuel:', fuel_on_hand, '| Position:', current_position, '| Task: Refueling', '| Steps:', steps, '| State:', state)

def move_and_drop(direction):
    global fuel_on_hand
    global fuel_taken
    global fuel_used
    global steps
    global current_position

    if (direction == 'back'):
        current_position -= 1
    elif (direction == 'forward'):
        current_position += 1

    fuel_on_hand -= 1
    fuel_used += 1
    if (current_position == 0):
        fuel_taken -= fuel_on_hand
    else:
        fuel_map[current_position] += fuel_on_hand
    fuel_on_hand = 0
    steps += 1
    print (fuel_map)
    print('Fuel:', fuel_on_hand, '| Position:', current_position, '| Task: Moving', direction, '| Steps:', steps, '| State:', state)

def carry_from_previous():
    global current_position
    global fuel_on_hand
    global fuel_taken
    global fuel_used
    global steps
    global fuel_map

    temp_geometric_sum = geometric_sum()

    while (fuel_map[current_position] < temp_geometric_sum):
        # Fill up truck
        take_fuel(1)
        # Move truck backwards and drop fuel
        move_and_drop('back')
        # Fill up truck
        take_fuel(3)
        # Move truck forward and drop fuel
        move_and_drop('forward')

    if (current_position == try_count):
        return()

    else:
        # Fill up truck
        take_fuel(3)
        # Move truck forward and drop fuel
        move_and_drop('forward')

        carry_from_previous()
        return()


print ('BEGIN \n')

# Checking if n == 1
# Fill up truck
take_fuel(2)
# Move truck forward and drop fuel
move_and_drop('forward')
# Check if destination reached
if (current_position == n):
    state = 'end'
else:
    state = 'returning'
    # Update map
    fuel_map.extend(zero_list_maker(1))
    # Update latest checked distance
    try_count = 1

# Main Loop
while (state != 'end'):

    while (state == 'returning'):
        # Fill up truck
        take_fuel(fuel_map[current_position])
        # Move truck
        move_and_drop('back')

        if (current_position == 0):
            state = 'exploring'

    while (state == 'exploring'):

        if (current_position == 0):
            # Fill up truck
            take_fuel(3)
             #Move truck forward and drop fuel
            move_and_drop('forward')
            carry_from_previous()

        if (current_position == (try_count + 1)):
            try_count += 1

            if (current_position == n):
                state = 'end'

            else:
                # Update map
                fuel_map.extend(zero_list_maker(1))
                print ('\nDestination not reached, insufficient fuel to progress, returning to base\n')
                state = 'returning'

        elif (current_position == try_count):
            # Fill up truck
            take_fuel(2)
            # Move truck forward and drop fuel
            move_and_drop('forward')

print ('\nCurrent Position is at destination, Mission Complete!\n')

print ('Mission took', (current_milli_time() - startTime), 'ms\n')

print ('::Results::')
print ('Fuel taken from start:', fuel_taken)
print ('Fuel actually used:', fuel_used)
