# DevOpsChallenge

Node.js application inside a Docker container. The task that I did was to deploy a separate docker container which requires a MySQL database to manage user data. 

MySQL Version 8

On the host which is running docker we should be able to use curl and get status:
● Return APP status: curl http://localhost/api/status
● Return User list: curl http://localhost/api/users


I also created a BASH script to monitor a log file. This log file will find keywords "ERROR" or "FAIL" and print an alert message.
