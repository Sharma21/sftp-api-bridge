import paramiko

def fetch_file_from_sftp(host, port, username, password, remote_path, local_path):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remote_path, local_path)
    sftp.close()
    transport.close()