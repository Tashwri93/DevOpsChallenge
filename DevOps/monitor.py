import time
from datetime import datetime, timedelta

# Specify the path to your log file
log_file_path = '/Users/tashan/Desktop/systems.log'  # Replace with your actual log file path

# Keywords to search for
keywords = ['ERROR', 'FAIL']

# Function to parse the timestamp from a log entry
def parse_timestamp(line):
    try:
        # Assuming the log format starts with a timestamp like "Aug 17 09:15:23"
        return datetime.strptime(line[:15], '%b %d %H:%M:%S')
    except ValueError:
        return None

# Get the current year to append to log timestamps
current_year = datetime.now().year

def monitor_log():
    with open(log_file_path, 'r') as file:
        # Move the pointer to the end of the file to monitor new entries
        file.seek(0, 2)
        
        # Continuously monitor the file
        while True:
            line = file.readline()
            if line:
                # Debug: Print the raw line read from the log file
                print(f"Read line: {line.strip()}")
                
                timestamp = parse_timestamp(line)
                if timestamp:
                    # Debug: Print the parsed timestamp
                    print(f"Parsed timestamp: {timestamp}")
                    
                    # Append the current year to the parsed timestamp
                    timestamp = timestamp.replace(year=current_year)
                    
                    # Check if the log entry is within the last 10 minutes
                    if timestamp >= datetime.now() - timedelta(minutes=10):
                        # Check if any keyword is in the line
                        if any(keyword in line for keyword in keywords):
                            print("ALERT: Error detected in the logs!")
                            print(f"Keyword found: {line.strip()}")
            else:
                # Wait for new log entries to be written to the file
                time.sleep(1)

# Start monitoring the log file
if __name__ == "__main__":
    monitor_log()
