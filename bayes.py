#bayes calculator

#data from tables
pClist = [.0001, .001, .001, .0001, .001]
pBClist = [.9, .9, .9, .95, .95]
pBCprimelist = [.001, .001, .01, .001, .01]

for x in range(0,5):
    top = pClist[x]*pBClist[x]
    bottom = (1-pClist[x])*pBCprimelist[x]

    result = top/bottom

    print("RESULT ", x,":")
    print(result)




#manual calculation
'''
print("")
print("p(C):")
pC = float(input())
print("P(B|C):")
pBC = float(input())
print("p(B|C`):")
pBCprime = float(input())


top = pC*pBC
bottom = (1-pC)*pBCprime

result = top/bottom

print("RESULT:")
print(result)
'''




