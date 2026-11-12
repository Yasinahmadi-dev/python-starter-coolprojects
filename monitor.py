import psutil 
from datetime import datetime 


CPU_THRESHOLD = 80
RAM_THRESHOLD = 85
DISK_THRESHOLD = 90

#check CPU USAGE over a 1-second window 
cpu_percent = psutil.cpu_percent(interval=1)

#Check RAM (memory) statistics
memory = psutil.virtual_memory()

disk = psutil.disk_usage("C:\\")

#Convert raw bytes to Gigabytes and round to 2 decimal places
free_gb = round(disk.free / (1024**3), 2)
total_gb = round(disk.total / (1024**3), 2)


print(f"Current CPU Usage: {cpu_percent}%")
print(f"Total RAM Usage: {memory.percent}%")
print(f"Current CPU Usage: {cpu_percent}%")
print(f"Total RAM Usage: {memory.percent}")
print(f"C: Drive Used: {disk.percent}% ({free_gb} GB free of {total_gb} GB)")


alerts = []

if cpu_percent > CPU_THRESHOLD:
    alerts.append(f"HIGH CPU LOAD: {cpu_percent}%")

if memory.percent > RAM_THRESHOLD:
    alerts.append(f"HIGH RAM USAGE: {memory.percent}%")

if disk.percent > DISK_THRESHOLD:
    alerts.append(f"LOW DISK SPACE: {disk.percent}% used")

if alerts:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_alerts.log", mode="a") as log_file:
        for alert in alerts:
            log_line = f"[{timestamp}] WARNING: {alert}\n"
            log_file.write(log_line)
            print(f"Logged Alert: {log_line.strip()}")
else:
    print("All systems healthy. No alerts triggered.")            

