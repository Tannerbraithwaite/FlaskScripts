import pysftp as sftp
def push_file_to_server():
    s = sftp.Connection(host='IP address', username='root', password='your password')
    local_path = 'testme.txt'
    remote_path = '/home/testme.txt'
    s.put(local_path, remote_path)
    s.close()


def get_file_from_server():
    s = sftp.Connection(host='IP address', username='root', password='your password')
    local_path = 'testme.txt'
    remote_path = '/home/testme.txt'
    s.get(remote_path, local_path)
    s.close()
