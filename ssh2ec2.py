import subprocess

# Set the path to your private key file
private_key_path = "C:/path/to/your/private/key.ppk"

# Set the path to your local file
local_file_path = "C:/path/to/your/local/file.txt"

# Set the username and IP address of your EC2 instance
username = "ec2-user"
ip_address = "X.X.X.X"  # Replace with your EC2 instance's IP address

# Set the path to your remote directory on the EC2 instance
remote_dir_path = "/home/ec2-user/files"

# Build the command to transfer the file
command = f"pscp -i {private_key_path} {local_file_path} {username}@{ip_address}:{remote_dir_path}"

# Execute the command
subprocess.call(command, shell=True)
