#!/usr/bin/env python3
import shutil
import psutil
import os
import sys

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_disk_usage(dir, min_percents):
     """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(dir)
    du_free_percent = 100*du.free/du.total

    return du_free_percent > min_percent

def main():
    if not check_disk_usage("/", 20):
        print("ERROR! Please check your disk space")
        sys.exit(1)
    elif check_cpu_usage():
        print("ERROR! Please check your CPU usage and performance")
        sys.exit(1)
    print("Everything OK!")
    sys.exit(0)

main()
