import numpy as np
from PIL import Image
im = Image.open("D:\Prototype\Bikesgray.jpg")
im.show()

print(list(np.asarray(im)))
Image.fromarray(np.asarray(im))