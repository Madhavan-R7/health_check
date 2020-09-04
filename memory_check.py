#!/usr/bin/env python3
import shutil
import psutil
import os
import sys

def check_disk_usage():
    raise("Please check the parameters!")
    sys.exit(1)

def check_disk_usage(dir, min_percent, min_gb):
    du = shutil.disk_usage(dir)
    du_free_percent = 100*du.free/du.total
    du_free_gb = du.free/2**30

    if du_free_percent <= min_percent or du_free_gb <=min_gb:
        return True
    return False

def main():
    if check_disk_usage("/", 20, 10):
        print("ERROR! Please check your disk space")
        sys.exit(1)
    print("Everything OK!")
    sys.exit(0)

main()
