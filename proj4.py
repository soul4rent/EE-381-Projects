import math
import matplotlib.pyplot as plt; plt.rcdefaults()#import graph stuff
import numpy as np
import matplotlib.pyplot as plt



def nCr(n,r):           #n choose r
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def binDistro(n, x, p):
    return nCr(n, x) * (p**x) * (1-p)**(n-x) #binomal distro formula
    

n = 18
p = 0.5


distro = []

for e in range(0,n+1):  #calculate each X in distribution
    distro.append(binDistro(n,e,p))
    #print(ans[e])


#===GRAPHING===

successes = range(n+1)
y_pos = np.arange(len(successes))
     
plt.bar(y_pos, distro, align='center', alpha=0.5)
plt.xticks(y_pos, successes)
plt.ylabel('Probability')
plt.title('Distribution (number of successes)')
     
plt.show()

#===============


#Part 2
for e in range(0,n+1):
    print(str(e)+":")
    print(sum(distro[e:])) #sum of all values from e to the end


    #13 looks (somewhat) close to 0.05
    #13 = CV? 
#================

distroTwo = []
Betas = []


for e in range(55, 105, 5):

    distro = []

    for i in range(0,n+1):
        pTilda = e/100
        distro.append(binDistro(18,i,pTilda))

    Betas.append(sum(distro[:13])) #everything before 13 (CV-1)




OneMinusBeta = [] #values of 1-Beta

for e in range(0, len(Betas)):
    #print(Betas[e])
    OneMinusBeta.append(1-Betas[e])


#===GRAPHING===
z = range(55, 105, 5)

y_pos = np.arange(len(z))
     
plt.bar(y_pos, OneMinusBeta, align='center', alpha=0.5)
plt.xticks(y_pos, z)
plt.ylabel('1-Beta')
plt.title('1-Beta VS PTilda')
     
plt.show()

#===============
    
    
    

