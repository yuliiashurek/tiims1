import matplotlib.pyplot as plt


def box(array):
    plt.boxplot(array, showmeans=True, labels=['Data'])
    plt.title('Box plot')
    plt.show()
