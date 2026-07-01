import shutil
import psutil

print("\n SYSTEM HEALTH DASHBOARD ")
print("-" * 40)

# 1. Using shutil: Check free disk space
# ("/" represents the root/main system drive, like C: on Windows)
disk_space = shutil.disk_usage("/")
free_space_gb = disk_space.free / (1024 ** 3) # Converting Bytes to Gigabytes (GB)
print(f" Free Disk Space : {free_space_gb:.2f} GB")

# 2. Using psutil: Check CPU usage percentage
# (interval=1 means it will monitor the CPU for 1 second to get accurate data)
cpu_usage = psutil.cpu_percent(interval=1)
print(f" CPU Usage       : {cpu_usage}%")

# 3. Using psutil: Check battery status
# (This will return 'None' if running on a desktop without a battery)
battery = psutil.sensors_battery()

if battery:
    print(f" Battery Level   : {battery.percent}%")
    if battery.power_plugged:
        print(" Power Status    : Charging (Plugged In)")
    else:
        print(" Power Status    : On Battery (Not Plugged In)")
else:
    print(" Battery Level   : No battery detected (Desktop System)")

print("-" * 40)