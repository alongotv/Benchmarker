import matplotlib.pyplot as plt


def generate_report(benchmark_entries: list):
    y = range(len(benchmark_entries))
    x = [elem.date_time for elem in benchmark_entries]
    (fig, ax) = plt.subplots(1, 1)
    ax.plot(x, y)
    fig.savefig('./generated/plot.png')

    # for entry in benchmark_entries:
