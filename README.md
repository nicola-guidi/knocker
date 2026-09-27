```
██╗  ██╗███╗   ██╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║ ██╔╝████╗  ██║██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
█████╔╝ ██╔██╗ ██║██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██╔═██╗ ██║╚██╗██║██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██╗██║ ╚████║╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

A lightweight, multi-threaded TCP port scanner written in pure Python, designed for authorized network reconnaissance and security assessments.

## Legal Disclaimer

**This tool is intended for ethical and authorized security testing only.**

The author assumes no responsibility for any misuse of this software. Scanning hosts or networks without explicit authorization is illegal and may result in criminal or civil penalties. Always ensure you have proper permission before conducting any security assessments.

## Overview

Knocker.py is a small port scanner built entirely on Python's standard library, with no external dependencies. It automatically recognizes whether to run a single-port check or a threaded range scan based on the parameters provided, and returns a clear per-port status.

## Key Features

- **Dual Scan Modes**: Automatically adapts to a single port or a full port range
- **Multi-Threaded**: Concurrent scanning across a range for faster results
- **Zero Dependencies**: Runs on the Python standard library alone
- **Robust Validation**: Comprehensive input checking for IP addresses and port numbers
- **Clear Status Output**: Reports each port as OPEN, CLOSED, TIMEOUT or UNKNOWN
- **Timeout Protection**: Built-in connection timeout handling to prevent hanging

## Requirements

- Python 3.6+
- No external libraries required

## Installation

```bash
git clone https://github.com/nicola-guidi/knocker.git
cd knocker
```

## Usage

### Basic Syntax

```bash
python3 knocker.py -i [TARGET IP] [OPTIONS]
```

### Command-Line Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--ip <IP address>` | `-i` | Target IP address (default: 127.0.0.1) |
| `--port <port>` | `-p` | Single port to scan |
| `--ports <range>` | `-P` | Port range to scan (e.g. `1-1000`) |

### Complete Usage Examples

**Scan a single port:**
```bash
python3 knocker.py -i 192.168.1.100 -p 80
```

**Scan a port range:**
```bash
python3 knocker.py -i 192.168.1.100 -P 1-1000
```

## License

This project is provided for educational and ethical security testing purposes only. Use this tool only on systems you own or have explicit permission to test.

## Author

Created by **Nicola Guidi**
