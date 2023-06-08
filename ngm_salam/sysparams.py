import platform
import os
import time
import psutil


def get_uptime():
    now = time.time()
    boottime = psutil.boot_time()
    uptime = (now - boottime) / 3600
    return int(uptime)


def get_hostname():
    return platform.node()


def get_username():
    user = os.getenv("USER")
    # return os.getlogin()
    return user


def get_cpu_count():
    return os.cpu_count()


def get_ram_size():
    ram = psutil.virtual_memory().total / (1024 * 1024 * 1024)
    return ram


# Example usage
print("Uptime:", get_uptime(), "hours")
print("Hostname:", get_hostname())
print("Username:", get_username())
print("CPU Count:", get_cpu_count())
print("RAM Size:", get_ram_size(), "GB")
