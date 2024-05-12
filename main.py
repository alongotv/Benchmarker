#!/usr/bin/env python
import benchmark
import report_generator
import time

benchmark.system_info()

benchmark_entries = list()

try:
    while True:
        bench_entry = benchmark.collect_usage_data()
        benchmark_entries.append(bench_entry)
        time.sleep(1)
except KeyboardInterrupt:
    pass

report_generator.generate_report(benchmark_entries)
