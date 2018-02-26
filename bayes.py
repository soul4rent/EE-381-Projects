#bayes calculator

print("p(C):")
pC = float(input())
print("P(B|C):")
pBC = float(input())
print("p(B|C`):")
pBCprime = float(input())


#bayes formula
top = pC*pBC
bottom = (1-pC)*pBCprime

result = top/bottom

print("RESULT:")
print(result)
