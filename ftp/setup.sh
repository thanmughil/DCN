#!/bin/bash

# Install vsftpd if not already installed
sudo apt-get update
sudo apt-get install vsftpd

# Create a new user account
sudo adduser ftpuser

# Set a password for the user
sudo passwd ftpuser

# Configure vsftpd to allow local users to log in
sudo sed -i 's/local_enable=NO/local_enable=YES/' /etc/vsftpd.conf

# Restart vsftpd
sudo service vsftpd restart

echo "FTP server setup complete."
