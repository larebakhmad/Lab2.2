from collections import defaultdict
import re
def ipdict(line):
    match = re.search(r'from ([0-9.]+)', line)
    if match:
        return match.group(1)
    return None
counts = defaultdict(int)
with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ipdict(line)
            if ip:
                counts[ip] += 1
print(counts)
"""
this program reads a log file and counts failed login attempts by IP address.
It uses regular expressions to extract IP addresses and a defaultdict to count occurrences. 
"""