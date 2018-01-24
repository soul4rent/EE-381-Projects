# general gist of pseudorandom number generators
# 1/24/2018
# Exploration of pseudorandom number generators
#
# Below the parameters in the formula are assigned their values.
import math

while True:
    
    mult = 41
    adder = 31
    norm = 100
    seed = int(input("Seed:"))

    numberGenerated = int(input("Amt of Numbers:"))

    #Below is the formula

    for x in range(1, numberGenerated+1):
        seed = (mult * seed + adder)%norm

        r = seed/norm
        print('%.3f'%r)

        number = math.floor(r*6+1)
        print(number)

    print("-------------------------")
