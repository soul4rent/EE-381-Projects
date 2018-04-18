#simulate binomial random variable, uses sum to simulate b.r.t
import random

n = 5 #number of trials
x = 3 #the number of desired successes
p = 0.7 #probability of success for any outcome

N = 7000000 #the number of times the process is repeated

trial = [0]
trial = trial*n #empty trial list


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

    if (s==x):
        j = j+1


prob = j/N
print("probability:")
print(prob)


#part Two
print("Calculated Expected value (Mu):")
print(n*p)

print("Experimental average value (xbar):")
print(sum(muCalc) / N)

