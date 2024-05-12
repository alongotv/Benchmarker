import matplotlib.pyplot as plt


def generate_report(benchmark_entries: list):
    # y = range(len(benchmark_entries))
    x = [elem.date_time for elem in benchmark_entries]
    y_cpu = [elem.cpu_percentage for elem in benchmark_entries]

    (fig, ax) = plt.subplots()
    twin1 = ax.twinx()
    twin2 = ax.twinx()
    ax.set_ylim(0, 100)

    p1, = ax.plot(x, y_cpu, "b-", label="CPU Load")
    fig.savefig('./generated/plot.png')

    # for entry in benchmark_entries:
