import string
import matplotlib.pyplot as plt
from pathlib import Path
from sys import getsizeof
import os
import csv


def generate_report(benchmark_entries: list):
    if len(benchmark_entries) == 0:
        print("Nothing to report: no data received")
        return

    print("The benchmark has collected ", getsizeof(benchmark_entries), "bytes of data")

    report_time = benchmark_entries[0].date_time.replace(microsecond=0).isoformat()
    directory_name = "Report-{0}".format(report_time)
    path_name = "./generated/{0}".format(directory_name)
    Path(path_name).mkdir(parents=True, exist_ok=True)

    x = [elem.date_time for elem in benchmark_entries]
    y_cpu = [elem.cpu_percentage for elem in benchmark_entries]
    y_ram = [elem.ram_usage.percent for elem in benchmark_entries]
    y_swap = [elem.swap_usage.percent for elem in benchmark_entries]
    y_swap_total = [elem.swap_usage.total / (1 << 20) for elem in benchmark_entries]
    y_swap_used = [elem.swap_usage.used / (1 << 20) for elem in benchmark_entries]

    draw_plots(x, y_cpu, y_ram, y_swap, y_swap_total, y_swap_used, path_name)
    generate_csv(x, y_cpu, y_ram, y_swap, y_swap_total, y_swap_used, path_name)

    print("Path to generated report: ", os.path.abspath(path_name))


def draw_plots(x, y_cpu, y_ram, y_swap, y_swap_total, y_swap_used, path_name: string):
    draw_main_plot(x, y_cpu, y_ram, y_swap, path_name)
    draw_swap_plot(x, y_swap_total, y_swap_used, path_name)


def draw_main_plot(x, y_cpu, y_ram, y_swap, path_name: string):
    (fig, ax) = plt.subplots(layout='constrained')
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
    ax.tick_params(axis='x', labelrotation=90)
    ax.legend(handles=[p1, p2, p3])

    fig.savefig('{0}/main_plot.png'.format(path_name))


def draw_swap_plot(x, y_swap_total, y_swap_used, path_name):
    (fig, ax) = plt.subplots(layout='constrained')
    twin1 = ax.twinx()

    max_swap_allocated = max(y_swap_total)
    ax.set_ylim(bottom=0)
    twin1.set_ylim(bottom=0)

    if max_swap_allocated > 0:
        ax.set_ylim(top=max_swap_allocated)
        twin1.set_ylim(top=max_swap_allocated)

    p1, = ax.plot(x, y_swap_total, "b-", label="SWAP Allocated (megabytes)")
    p2, = twin1.plot(x, y_swap_used, "r-", label="SWAP Usage (megabytes)")

    ax.set_xlabel("Time")
    ax.set_ylabel("SWAP Usage (megabytes)")
    ax.tick_params(axis='x', labelrotation=90)
    ax.legend(handles=[p1, p2])
    fig.savefig('{0}/swap_plot.png'.format(path_name))


def generate_csv(x, y_cpu, y_ram, y_swap, y_swap_total, y_swap_used, path_name: string):
    headers = ['time', 'cpu_usage_percentage', 'ram_used_percentage', 'swap_used_percentage', 'swap_allocated',
               'swap_used']
    file_name = '{0}/benchmark_logs.csv'.format(path_name)

    arr = [x, y_cpu, y_ram, y_swap, y_swap_total, y_swap_used]

    # Rotate the matrix by 90 degrees
    arr_rotated = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]) - 1, -1, -1)]

    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(arr_rotated)
