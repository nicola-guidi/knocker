import socket
import argparse
import sys
import errno
import threading

parser = argparse.ArgumentParser(
    prog="knocker.py",
    description="Lightweight port scanner",
    epilog="Enjoy!",
    usage="python3 knocker.py [options]",
    add_help=True
)

group = parser.add_mutually_exclusive_group()
parser.add_argument("-i", "--ip", default="127.0.0.1", help="IP to scan")
group.add_argument("-p", "--port", help="port to scan")
group.add_argument("-P", "--ports", help="port range to scan")

args = parser.parse_args()

if args.ports:
    parts = args.ports.split("-")
    if len(parts) != 2:
        print("Invalid port range")
        sys.exit()
    else:
        first_port = parts[0]
        end_port = parts[1]

def validate_port(port):
    try:
        port_int = int(port)
        if port_int in range(1, 65536):
            return port_int
        else:
            print("Port must be between 1 and 65535")
    except ValueError:
        print("Port must be an integer")

def validate_port_range(first_port, end_port):
    try:
        first_port_int = int(first_port)
        end_port_int = int(end_port)
        if first_port_int not in range(1, 65536) or end_port_int not in range(1, 65536):
            print("Port must be between 1 and 65535")
        elif first_port_int >= end_port_int:
            print("Port range must be incremental")
        else:
            return first_port_int, end_port_int
    except ValueError:
        print("Port must be an integer")

print("Scanning target IP {}".format(args.ip))

def port_scan(i, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        result_int = s.connect_ex((i, p))
        if result_int == 0:
            result_string = "OPEN"
        elif result_int == errno.ECONNREFUSED:
            result_string = "CLOSED"
        else:
            result_string = "UNKNOWN"
    except TimeoutError:
        result_string = "TIMEOUT"
    finally:
        s.close()
    return result_string

def scan_and_store(i, port, results):
    result = port_scan(i, port)
    results.append((port, result))

def port_range_scan(i, p1, p2):
    results = []
    threads = []
    for port in range(int(p1), int(p2) + 1):
        thread = threading.Thread(target=scan_and_store, args=(i, port, results))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return(results)

if args.port:
    port = validate_port(args.port)
    if port is not None:
        result_string = port_scan(args.ip, port)
        if result_string == "OPEN":
            print("Port {} is open".format(args.port))
        elif result_string == "TIMEOUT":
            print("Port {} timed out".format(args.port))
        else:
            print("Port {} is unknown".format(args.port))
elif args.ports:
    port_range = validate_port_range(first_port, end_port)
    if port_range is None:
        sys.exit()
    result_string = port_range_scan(args.ip, *port_range)
    for port, result in result_string:
        port = port
        result = result
        print(f"Port {port} is {result}")



