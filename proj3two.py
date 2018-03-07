#simulate binomial random variable, uses sum to simulate b.r.t
import random

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

n = 5 #number of trials
p = 0.7 #probability of success for any outcome

N = 10000 #the number of times the process is repeated

trial = [0]
trial = trial*n #empty trial list

probability = [0]
probability = probability * (n+1)

x=0

j = 0 #acc intitialized

E = 0 #acc for the average

for k in range (N): #number of times process is repeated
    for i in range (n): #number of trials
        r = random.uniform(0,1)
        if r < p:
            trial[i] = 1 #success
        else:
            trial[i] = 0 #failure

    s = sum(trial)

#oh dear
    if s==0:
        a = a+1
        probability[0] = a/N
    elif s == 1:
        b = b+1
        probability[1] = b/N
    elif s == 2:
        c = c+1
        probability[2] = c/N
    elif s == 3:
        d = d+1
        probability[3] = d/N
    elif s == 4:
        e = e+1
        probability[4] = e/N
    elif s == 5:
        f = f+1
        probability[5] = f/N


    
#        j = j+1


#prob = j/N
#probability[x] = prob
#print(prob)

import matplotlib.pyplot as plt
x = [0,1,2,3,4,5]
plt.bar(x,probability)
plt.show()

