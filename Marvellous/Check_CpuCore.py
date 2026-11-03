import os
import psutil
import platform

print(f"Processor: {platform.processor()}")
print(f"Total CPU Cores (Physical): {psutil.cpu_count(logical=False)}")
print(f"Total Logical Threads: {psutil.cpu_count(logical=True)}")
print(f"Current CPU Usage: {psutil.cpu_percent(interval=1)}%")