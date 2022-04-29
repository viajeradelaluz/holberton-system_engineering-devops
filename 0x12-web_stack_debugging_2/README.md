# 0x12. Web stack debugging #2

## Tasks

### **0. Run software as another user**

Requirements:

- Write a Bash script that accepts one argument
- The script should run the `whoami` command under the user passed as an argument
- Make sure to try your script by passing different users

### **1. Run Nginx as Nginx**

Fix the sandbox so that Nginx is running as the nginx user.

Requirements:

- `nginx` must be running as `nginx` user
- `nginx` must be listening on all active IPs on port `8080`
- You cannot use `apt-get remove`
- Write a Bash script that configures the container to fit the above requirements

### **2. 7 lines or less**

Using what you did for task #1, make your fix short and sweet.

Requirements:

- Your Bash script must be 7 lines long or less
- There must be a new line at the end of the file
- You respect Bash script requirements
- You cannot use `;`
- You cannot use `&&`
- You cannot use `wget`
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
