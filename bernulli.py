#simulate binomial random variable, uses sum to simulate b.r.t
import random


print("prob success:")
p = float(input())
print("num trials:")
N = int(input())

n = 5 #number of trials
x = 3 #the number of successes
#p = 0.7 #probability of success for any outcome

#N = 10000 #the number of times the process is repeated

trial = [0]
trial = trial*n #empty trial list

j = 0 #acc intitialized

for k in range(N): #number of times process is repeated
    #for i in range (n): #number of trials
        r = random.uniform(0,1)
        if r < p:
            #trial[k] = 1 #success
            print("Success")
        else:
            #trial[k] = 0 #failure
            print("Fail")

    #s = sum(trial)

    #if (s==x):
        #j = j+1


prob = j/N
print(prob)


