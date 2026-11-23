from collections import Counter
from statistics import median

#function to calculate the sum
def sum_number(numbers):
    return sum(numbers)

#function to calculate the average(mean)
def average_mean(numbers):
    return sum(numbers) /len(numbers)

# function to calculate the median and mode
def median_and_mode(numbers):
    med=median(numbers)

    counts = Counter(numbers)
    highest_frequency= max(counts.values())

    modes = [number for number, count in counts.items()
             if count ==
             highest_frequency]
    return med, modes

#list of numbers 
numbers = [1,1,5,2,4]

#diaplay the results
print("sum", sum_number(numbers))
print("average: ",
average_mean(numbers))

med, modes = median_and_mode(numbers)
print("median: ", med)
print("mode: ", modes)



