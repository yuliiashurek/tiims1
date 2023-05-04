import math


# calculate mean
def mean(array):
    n = len(array)

    get_sum = sum(array)
    result = get_sum / n
    print("Average is: " + str(round(result, 2)))


# calculate median
def median(array):
    n = len(array)
    array.sort()

    if n % 2 == 0:
        median1 = array[n // 2]
        median2 = array[n // 2 - 1]
        res = (median1 + median2) / 2
    else:
        res = array[n // 2]
    print("Median is: " + str(res))


# calculate mode
def mode(array):
    array.sort()

    l1 = []
    i = 0
    while i < len(array):
        l1.append(array.count(array[i]))
        i += 1
    d1 = dict(zip(array, l1))

    d2 = {k for (k, v) in d1.items() if v == max(l1)}
    print("Mode(s) is/are :" + str(d2))


# calculate sample variance
def variance(array):
    avg = sum(array) / len(array)
    var = sum((x - avg) ** 2 for x in array) / len(array)
    square = math.sqrt(var)
    print("Sample variance is: " + str(round(var, 2)))
    print("RMSD is: " + str(round(square, 2)))