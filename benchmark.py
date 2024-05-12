from datetime import datetime
import psutil


def generate_report():
    print("CPU core count", psutil.cpu_count())


def collect_usage_data():
    cpu_percentage = psutil.cpu_percent(interval=1)
    dt = datetime.now()
    print("entry time", dt)
    print("CPU Usage: ", cpu_percentage)
    vmem = psutil.virtual_memory()
    smem = psutil.swap_memory()
    print("RAM usage", vmem)
    print("SWAP Usage: ", smem)
