from datetime import datetime
import psutil


def some_func():
    print("CPU core count", psutil.cpu_count())


def collect_usage_data():
    dt = datetime.now()
    print("entry time", dt)
    print("CPU Usage: ", psutil.cpu_percent(interval=1))
    vmem = psutil.virtual_memory().percent
    # print("CPU Usage: ", psutil.cpu_percent())
    print("Ram usage", vmem)
