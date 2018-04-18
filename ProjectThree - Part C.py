#simulate binomial random variable, uses sum to simulate b.r.t
import random

import matplotlib.pyplot as plt; plt.rcdefaults()#import graph stuff
import numpy as np
import matplotlib.pyplot as plt

#n = 5 #number of trials
#x = 3 #the number of desired successes
#p = 0.5 #probability of success for any outcome

print("number of trials")
n = int(input(">"))
print("lower bound of successes")
lower = int(input(">"))
print("upper bound of successes")
upper = int(input(">"))
print("probability of success:")
p = float(input(">"))




N = 10000 #the number of times the process is repeated

trial = [0]
trial = trial*n #empty trial list


distro = [0]
distro = distro*(n+1) #for the bar graph and results


for yep in range(n+1): #for each number of successes

    muCalc = [0]
    muCalc = muCalc*N #for calcuating experimental average (part 2)

    j = 0 #acc intitialized
    for k in range(N): #number of times process is repeated
        for i in range (n): #number of trials
            r = random.uniform(0,1)
            if r < p:
                trial[i] = 1 #success
                #print("Success")
            else:
                trial[i] = 0 #failure
                #print("Fail")

        s = sum(trial)
        muCalc[k] = s #add number of successes to list of trials (for part 2)

        #if (s==x):
        if (s==yep):
            j = j+1


    prob = j/N
    print("probability:")
    print(prob)

    distro[yep] = prob #for bar graph

    


#part3
print("---------------------------")
print("distribution of data (from 0 to ",n,")")
print (distro)
print("experimental probability distribution of range (from ",lower," to ",upper,")")
print(distro[lower:(upper+1)])
print("Sum of range of experimental probabilities (from ",lower," to ",upper,")")
print(sum(distro[lower:(upper+1)]))
print("Calculated Expected value (Mu):")
print(n*p)
print("Experimental average value (xbar) of most recent trial:")
print(sum(muCalc) / N)

HELLO_KENOBI=input("Bar Graph? (y/n) ::") #star wars prequel meme
if (HELLO_KENOBI == "y"):
    successes = range(n+1)
    y_pos = np.arange(len(successes))
     
    plt.bar(y_pos, distro, align='center', alpha=0.5)
    plt.xticks(y_pos, successes)
    plt.ylabel('Probability')
    plt.title('Distribution (number of successes)')
     
    plt.show()
