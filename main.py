#!/usr/bin/env python
import benchmark
import time

try:
    while True:
        bench_entry = benchmark.collect_usage_data()
        print(bench_entry)
        time.sleep(1)
except KeyboardInterrupt:
    pass


benchmark.generate_report()