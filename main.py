#!/usr/bin/env python
import benchmark
import time

try:
    while True:
        benchmark.collect_usage_data()
        time.sleep(1)
except KeyboardInterrupt:
    pass


benchmark.generate_report()