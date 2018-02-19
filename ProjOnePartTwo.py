#tutorial on determining summary statistics



import statistics

numbers = []
#user inputs data


while True:
    try:
        n = int(input("enter num: "))
        numbers.append(n)
    except ValueError:
        break

s = sum(numbers)
N = len(numbers)
#caclulate the mean
mean = s/N
print("Mean:", mean)
#calculate the median
numbers.sort()

if N%2 == 0: #even number of datums
    mone = N/2
    mtwo = (N/2)+1

    mone = int(mone)-1
    mtwo = int(mtwo)-1

    median = (numbers[mone] + numbers[mtwo])/2

else:
    m = (N+1)/2
    m = int(m)-1
    median = numbers[m]

print("Median (manual): ", median)
print("median: ", statistics.median(numbers)) #debug


#calculate mode
from collections import Counter

c = Counter(numbers)
mode = c.most_common(1)
print(mode)


#standard deviation
import math

for x in numbers
    y = (x - mean)**2
    a = a+y
sigma = math.sqrt(a/N)
print(sigma)
