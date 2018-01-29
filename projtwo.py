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
print("median: ", statistics.median(numbers))
