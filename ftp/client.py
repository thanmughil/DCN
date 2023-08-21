from ftplib import FTP

def upload_file(ftp, local_path, remote_filename):
    with open(local_path, 'rb') as local_file:
        ftp.storbinary(f'STOR {remote_filename}', local_file)

def download_file(ftp, remote_filename, local_path):
    with open(local_path, 'wb') as local_file:
        ftp.retrbinary(f'RETR {remote_filename}', local_file.write)

def main():
    # FTP server credentials and details
    ftp_server = 'ftp.dlptest.com'
    username = 'dlpuser'
    password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    remote_directory = '/'
    
    # Local file to upload and download
    local_file_to_upload = 'C:\\Users\\kthan\\Pictures\\Camera Roll\\Sanjay S.jpg'
    local_file_to_download = 'C:\\Users\\kthan\\Pictures\\Camera Roll\\remote_file.txt'
    
    # Connect to the FTP server
    ftp = FTP(ftp_server)
    ftp.login(username, password)
    
    # Upload a file
    upload_file(ftp, local_file_to_upload, '/remote_file.jpg')
    
    # Download a file
    download_file(ftp, '/BunkerWestProdProxiesResFile_bwbluecoat2_2023-08-21-02-30-03.txt', local_file_to_download)
    
    # List files in remote directory
    file_list = ftp.nlst(remote_directory)
    for i in file_list:
        print("List of files in remote directory:", i)
    
    # Close the FTP connection
    ftp.quit()

if __name__ == "__main__":
    main()
