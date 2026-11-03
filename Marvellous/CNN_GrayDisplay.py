from PIL import Image
import numpy as np

img = Image.open("digit_28x28.png")

img = img.convert("L")

img = img.resize((28,28))

pixels = np.array(img)

print("omage size :",pixels.shape)

print("Pixels values :")

print(pixels)

#  0  pure black
# 255 pure white
# 50  dark gray
# 120 medium gray
# 200 light gray