#tutorial on determining summary statistics


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
