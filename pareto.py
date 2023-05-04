import matplotlib.pyplot as plt


def pareto(arr):
    # calculate frequency of each unique value
    freq_dict = {}
    for val in arr:
        freq_dict[val] = freq_dict.get(val, 0) + 1

    # sort dictionary by frequency in descending order
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # calculate cumulative sum of frequencies and total count
    cum_sum = 0
    total_count = len(arr)
    cumulative_percentages = []
    for val, freq in sorted_freq:
        cum_sum += freq
        percent = (cum_sum / total_count) * 100
        cumulative_percentages.append(percent)


    # plot Pareto chart
    fig, ax1 = plt.subplots()

    ax1.bar(range(len(sorted_freq)), [val[1] for val in sorted_freq], align='center')
    ax1.set_xticks(range(len(sorted_freq)))
    ax1.set_xticklabels([str(val[0]) for val in sorted_freq])
    ax1.set_ylabel('Frequency')

    ax2 = ax1.twinx()
    ax2.plot(range(len(sorted_freq)), cumulative_percentages, '-ro', markersize=5)
    ax2.set_ylim([0, 100])
    ax2.set_ylabel('Cumulative Percentage')

    plt.title('Pareto Chart')
    plt.show()
