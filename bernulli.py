#simulate binomial random variable, uses sum to simulate b.r.t
import random

n = 5 #number of trials
x = 3 #the number of successes
p = 0.7 #probability of success for any outcome

N = 10000 #the number of times the process is repeated

trial = [0]
trial = trial*n #empty trial list

j = 0 #acc intitialized

for k in range (N): #number of times process is repeated
    for i in range (n): #number of trials
        r = random.uniform(0,1)
        if r < p:
            trial[i] = 1 #success
        else:
            trial[i] = 0 #probably redundant, but prof. code, not mine.

    s = sum(trial)

    if (s==x):
        j = j+1


prob = j/N
print(prob)


