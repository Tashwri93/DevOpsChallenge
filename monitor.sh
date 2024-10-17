#!/bin/bash

#The systems.log file provided for me
LOGFILE="/path/to/logfile.log"

# Get the current time and the time 10 minutes ago
current_time=$(date '+%b %d %H:%M:%S')
time_10_minutes_ago=$(date --date='10 minutes ago' '+%b %d %H:%M:%S')

#Funtion to read through the log file by line to extract the keywords from the file
process_logs() {
    while read -r line; do
        
        log_time=$(echo "$line" | awk '{print $1 " " $2}')

        # Check if the log time is within the last 10 minutes
        if [[ "$log_time" > "$time_10_minutes_ago" && "$log_time" < "$current_time" ]]; then
            echo "$line" | grep -i -E 'error|fail' && echo "ALERT: Error detected in the logs! - $line"
        fi
    done
}

# Monitor the log file 
tail -f "$LOGFILE" | process_logs

#Below is the commands i used to check how to monitor a file using real-time

#tail -f /path/to/your/logfile.log | grep -i -E 'error|fail'
#awk -v d="$(date --date='10 minutes ago' '+%b %d %H:%M:%S')" '$0 ~ d, 1' /path/to/your/logfile.log | grep -i -E 'error|fail'
#if awk -v d="$(date --date='10 minutes ago' '+%b %d %H:%M:%S')" '$0 > d' /path/to/your/logfile.log | grep -i -q -E 'error|fail'; then
 #   echo "ALERT: Error detected in the logs!"
#fi




