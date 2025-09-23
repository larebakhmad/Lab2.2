LOGFILE = "sample_auth_small.log"
import re
ip_set = set()
ips_found = []
line_count = 0
with open(LOGFILE, "r") as f:
    for line in f:
        line_count += 1
        ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
        for ip in ips:
            ips_found.append(ip)
            ip_set.add(ip)
        if len(ips_found) >= 10:
            break
    print(f"Lines read: {line_count}")
    print(f"Unique IPs: {len(ip_set)}")
    print("First 10 IPs:")
    print(ips_found[:10])
    """
    this program reads a log file line by line, extracts IP addresses using a regular expression.
    """