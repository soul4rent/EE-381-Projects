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

if N%2 == 0:
    mone = N/2
    mtwo = (N/2)+1

    mone = int(mone)-1
    mtwo = int(mtwo)-1

    median = (numbers[mone] + numbers[mtwo])/2

else:
    median = (N+1)/2

print("Median (manual): ", median)
print("median: ", statistics.median(numbers)) #debug
