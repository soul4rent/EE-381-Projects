# general gist of pseudorandom number generators
# 1/24/2018
# Exploration of pseudorandom number generators
#
# Below the parameters in the formula are assigned their values.

mult = 3
adder = 15
norm = 11
seed = 1

#Below is the formula

for x in range(1, 10):
    seed = (mult * seed + adder)%norm
    print(seed)
