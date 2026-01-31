import csv
from collections import Counter

THRESHOLD = 30

ip_counter = Counter()

with open("traffic.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        src_ip = row.get("ip.src")

        if src_ip:
            ip_counter[src_ip] += 1

print("Traffic volume per Source IP:\n")

for ip, count in ip_counter.items():
    print(f"{ip}: {count} packets")

print("\n[!] Potentially Suspicious Source IPs:\n")
for ip, count in ip_counter.items():
    if count > THRESHOLD:
        print(f"{ip} -> {count} packets (above threshold)")
