LOGFILE = "sample_auth_small.log"
def simple_parser(line):
    if " port " in line:
        parts = line.split()
        try:
            anchor = parts.index("port")
            port = parts[anchor+1]
            return port.strip()
        except (ValueError, IndexError):
            return None
    return None
if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            print (simple_parser(line.strip()))
            