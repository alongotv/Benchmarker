from datetime import datetime
import psutil


def generate_report():
    print("CPU core count", psutil.cpu_count())


def collect_usage_data():
    cpu_percentage = psutil.cpu_percent()
    dt = datetime.now()
    vmem = psutil.virtual_memory()
    smem = psutil.swap_memory()
    return BenchEntry(date_time=dt, cpu_percentage=cpu_percentage, ram_usage=vmem, swap_usage=smem)


class BenchEntry:
    date_time = None
    cpu_percentage = None
    ram_usage = None
    swap_usage = None

    def __init__(self, date_time, cpu_percentage, ram_usage, swap_usage):
        self.date_time = date_time
        self.cpu_percentage = cpu_percentage
        self.ram_usage = ram_usage
        self.swap_usage = swap_usage

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
