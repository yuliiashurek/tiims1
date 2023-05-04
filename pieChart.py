import matplotlib.pyplot as plt


def pie(array):
    # Step 1: Calculate frequency of each unique value in array
    freq = {}
    for num in array:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Sort dictionary in descending order of frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Extract keys and values as separate lists
    labels, values = zip(*sorted_freq)

    # Step 4: Create pie chart
    plt.pie(values, labels=labels)
    plt.title('Pie chart')
    plt.show()
