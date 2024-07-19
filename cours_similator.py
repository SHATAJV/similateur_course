#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Course Similator:
"""

import random
total_distance = 2400
min_number_horses = 12
max_number_horses =20

def start_dice():
    return  random.randint(1, 6)
def Speed(currenct_speed, DQ):
     if DQ:
         return currenct_speed, DQ
     dice=start_dice()
     if currenct_speed ==0:
         if dice ==1 or dice==2:
             DQ= True
     elif currenct_speed ==1:
         if dice==1:
             currenct_speed +=1
     elif currenct_speed==2:
         if dice in [1,2]:
             currenct_speed +=1
     elif currenct_speed==3:
         if dice in [4,5]:
             currenct_speed +=1
         elif dice==1:
             currenct_speed -=1
     elif currenct_speed==4:
         if dice==1:
             currenct_speed -=1
     elif currenct_speed==5:
         if dice in [1,2]:
             currenct_speed -=1
     elif currenct_speed ==6:
         if dice in [1,2]:
             currenct_speed -=1
         elif dice==6:
             DQ=True

     if currenct_speed<0:
         currenct_speed

     return currenct_speed,DQ

def position_horse (position, speed, DQ):
    for i, pos in enumerate(position):
        status = "DQ" if DQ[i] else f"Position: {pos} m, Speed: {speed[i]} m/s"
    print(f"Horse {i+1} - {status}")
def winner(positions):
    for i, pos in enumerate(positions):
        if pos >= total_distance:
            return i
            return None


def main():


    while True:
        try:
            num_horses = int(input(f"Enter the number of horses ({min_number_horses} to {max_number_horses}): "))
            if min_number_horses <= num_horses <= max_number_horses:
                break
            else:
                print(f"Please enter a number between {min_number_horses} and {max_number_horses}.")
        except ValueError:
            print("Please enter a valid number.")
    positions = [0] * num_horses
    speeds = [0] * num_horses
    DQ = [False] * num_horses

    while True:
        input("Press Enter to advance the race by one turn...")

        for i in range(num_horses):
            if not DQ[i]:
                speeds[i], DQ[i] = Speed(speeds[i], DQ[i])
                positions[i] += speeds[i]

        position_horse(positions, speeds, DQ)

        winning_horse = winner(positions)
        if winning_horse is not None:
            print(f"Horse {winning_horse + 1} has won the race!")
            break

if __name__ == "__main__":
    main()
