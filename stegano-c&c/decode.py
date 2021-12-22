# Fabian Ferristo Tirtabudi - 2301864581 #

import base64
import stegano

IMAGE_TO_DECODE = "image_with_result.png"

encoded_result = stegano.lsb.reveal(IMAGE_TO_DECODE)
decoded_result = base64.b64decode(encoded_result.encode()).decode()

print("\n-----------------------------------------------------------------")
print("Result found from image: \n" + decoded_result)
print("-----------------------------------------------------------------")
