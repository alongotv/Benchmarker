import matplotlib.pyplot as plt
from pathlib import Path


def generate_report(benchmark_entries: list):
    if len(benchmark_entries) == 0:
        print("Nothing to report: no data received")
        return
    x = [elem.date_time for elem in benchmark_entries]
    y_cpu = [elem.cpu_percentage for elem in benchmark_entries]
    y_ram = [elem.ram_usage.percent for elem in benchmark_entries]
    y_swap = [elem.swap_usage.percent for elem in benchmark_entries]

    (fig, ax) = plt.subplots()
    twin1 = ax.twinx()
    twin2 = ax.twinx()
    ax.set_ylim(0, 100)
    twin1.set_ylim(0, 100)
    twin2.set_ylim(0, 100)

    p1, = ax.plot(x, y_cpu, "b-", label="CPU Load")
    p2, = twin1.plot(x, y_ram, "r-", label="RAM Usage")
    p3, = twin2.plot(x, y_swap, "g-", label="SWAP Usage")

    ax.set_xlabel("Time")
    ax.set_ylabel("Load (in %)")

    ax.legend(handles=[p1, p2, p3])

    report_time = benchmark_entries[0].date_time.replace(microsecond=0).isoformat()
    directory_name = "Report {0}".format(report_time)
    Path("./generated/{0}".format(directory_name)).mkdir(parents=True, exist_ok=True)

    fig.savefig('./generated/{0}/plot.png'.format(directory_name))

    # for entry in benchmark_entries:
