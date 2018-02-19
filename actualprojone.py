#Random Number Generator

#Below are fixed values for the Rand Num Generator

N = 10000
A = 4857
M = 8601
S = int(input("enter value for seed: "))

k = int(input("Enter the number of random numbers you want: "))

a = 0 #used for avg
for i in range(1,k+1):
    S = (M * S + A)%N
    r = S/N #random numbers between 0 and 1
    print(format('%.4f'%r))

    a = a+r

average = a/k
print("average: ", average)
    
