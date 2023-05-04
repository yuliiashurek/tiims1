import matplotlib.pyplot as plt


def polygonAndHistogram(x):
    a, bins, c = plt.hist(x, bins=7, histtype='step')
    l = list(bins)
    l.insert(0, 0)
    l.insert(len(bins) + 1, bins[len(bins) - 1])
    mid = []
    for i in range(len(l) - 1):
        ele = (l[i] + l[i + 1]) / 2
        mid.append(ele)
    x = list(a)
    x.insert(0, 0)
    x.insert(len(a) + 1, 0)
    plt.plot(mid, x, 'go--')
    plt.xlabel("Intervals")
    plt.ylabel("Frequency")
    plt.title("Polygon&Histogram")
    plt.show()
