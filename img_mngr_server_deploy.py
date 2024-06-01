import requests
import paramiko
import os

class ServerImageManager:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def download_image(self, image_id, destination):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(f'{self.api_url}/images/{image_id}/download', headers=headers)
        if response.status_code == 200:
            with open(destination, 'wb') as file:
                file.write(response.content)
            return True
        return False

    def deploy_image_to_server(self, server_ip, username, password, image_path):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(server_ip, username=username, password=password)
            # Assuming the image is a disk image file to be copied
            sftp = ssh.open_sftp()
            sftp.put(image_path, '/tmp/server_image.iso')
            sftp.close()
            # Execute deployment commands
            stdin, stdout, stderr = ssh.exec_command('sudo dd if=/tmp/server_image.iso of=/dev/sda')
            print(stdout.read())
            ssh.close()
            return True
        except Exception as e:
            print(f"Failed to deploy image: {e}")
            return False
