import math

#Theory:
#5/5 * 4/5 * 3/5 ~ .48 (48%)
#probability ball will land in an empty can goes down each time a
#can fills up, thus the odds are reduced by 1/5 each time.



#random number generator

N = 100000 #norm
A = 4867 #adder
M = 8601 #multiplier
S = 0 #seed

Sum = 0 #intialize counter

Can = [0,0,0]

K = int(input("Enter the number of experiements: "))

for k in range(K):
    for i in range(3):
        S = (M * S + A)%N
        r = S/N #generate random number

        Can_Number = math.floor(r * 5 + 1) #store can number (5 cans)
        Can[i] = Can_Number

    if (i == 2) and ((Can[0] != Can[1]) and (Can[1] != Can[2]) and (Can[0] != Can[2])):
        Sum = Sum + 1

prob = Sum / K

print("The probability is: " + str(prob))
