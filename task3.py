from collections import defaultdict
import re
import time

def ip_parse(line):
    match = re.search(r'from ([0-9.]+)', line)
    if match:
        return match.group(1)
    return None

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

start = time.time()
counts = defaultdict(int)

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
end = time.time()

print("Top 5 attacker IPs:")
for i, (ip, count) in enumerate(top_n(counts, 5), 1):
    print(f"{i}. {ip} — {count}")

with open("failed_counts.txt", "w") as out:
    out.write("ip,failed_count\n")
    for ip, count in counts.items():
        out.write(f"{ip},{count}\n")
print("Wrote failed_counts.txt")
print("Elapsed:", round(end-start, 2), "seconds")
