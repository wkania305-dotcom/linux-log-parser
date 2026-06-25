import os

def analyze_logs(file_path):
    print(f"=== Starting Analysis for: {file_path} ===")
    if not os.path.exists(file_path):
        print("Error: Log file does not exist.")
        return

    critical_errors = 0
    with open(file_path, 'r') as file:
        for line in file:
            if "CRITICAL" in line or "ERROR 500" in line:
                print(f"[ALERT] Found issue: {line.strip()}")
                critical_errors += 1

    print("=========================================")
    print(f"Analysis complete. Total critical issues found: {critical_errors}")

# Example usage (simulated log file)
analyze_logs("server.log")
