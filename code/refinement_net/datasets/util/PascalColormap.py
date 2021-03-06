import numpy as np
from PIL import Image

pascal_colormap = [
    0     ,         0,         0,
    0.5020,         0,         0,
         0,    0.5020,         0,
    0.5020,    0.5020,         0,
         0,         0,    0.5020,
    0.5020,         0,    0.5020,
         0,    0.5020,    0.5020,
    0.5020,    0.5020,    0.5020,
    0.2510,         0,         0,
    0.7529,         0,         0,
    0.2510,    0.5020,         0,
    0.7529,    0.5020,         0,
    0.2510,         0,    0.5020,
    0.7529,         0,    0.5020,
    0.2510,    0.5020,    0.5020,
    0.7529,    0.5020,    0.5020,
         0,    0.2510,         0,
    0.5020,    0.2510,         0,
         0,    0.7529,         0,
    0.5020,    0.7529,         0,
         0,    0.2510,    0.5020,
    0.5020,    0.2510,    0.5020,
         0,    0.7529,    0.5020,
    0.5020,    0.7529,    0.5020,
    0.2510,    0.2510,         0,
    0.7529,    0.2510,         0,
    0.2510,    0.7529,         0,
    0.7529,    0.7529,         0,
    0.2510,    0.2510,    0.5020,
    0.7529,    0.2510,    0.5020,
    0.2510,    0.7529,    0.5020,
    0.7529,    0.7529,    0.5020,
         0,         0,    0.2510,
    0.5020,         0,    0.2510,
         0,    0.5020,    0.2510,
    0.5020,    0.5020,    0.2510,
         0,         0,    0.7529,
    0.5020,         0,    0.7529,
         0,    0.5020,    0.7529,
    0.5020,    0.5020,    0.7529,
    0.2510,         0,    0.2510,
    0.7529,         0,    0.2510,
    0.2510,    0.5020,    0.2510,
    0.7529,    0.5020,    0.2510,
    0.2510,         0,    0.7529,
    0.7529,         0,    0.7529,
    0.2510,    0.5020,    0.7529,
    0.7529,    0.5020,    0.7529,
         0,    0.2510,    0.2510,
    0.5020,    0.2510,    0.2510,
         0,    0.7529,    0.2510,
    0.5020,    0.7529,    0.2510,
         0,    0.2510,    0.7529,
    0.5020,    0.2510,    0.7529,
         0,    0.7529,    0.7529,
    0.5020,    0.7529,    0.7529,
    0.2510,    0.2510,    0.2510,
    0.7529,    0.2510,    0.2510,
    0.2510,    0.7529,    0.2510,
    0.7529,    0.7529,    0.2510,
    0.2510,    0.2510,    0.7529,
    0.7529,    0.2510,    0.7529,
    0.2510,    0.7529,    0.7529,
    0.7529,    0.7529,    0.7529,
    0.1255,         0,         0,
    0.6275,         0,         0,
    0.1255,    0.5020,         0,
    0.6275,    0.5020,         0,
    0.1255,         0,    0.5020,
    0.6275,         0,    0.5020,
    0.1255,    0.5020,    0.5020,
    0.6275,    0.5020,    0.5020,
    0.3765,         0,         0,
    0.8784,         0,         0,
    0.3765,    0.5020,         0,
    0.8784,    0.5020,         0,
    0.3765,         0,    0.5020,
    0.8784,         0,    0.5020,
    0.3765,    0.5020,    0.5020,
    0.8784,    0.5020,    0.5020,
    0.1255,    0.2510,         0,
    0.6275,    0.2510,         0,
    0.1255,    0.7529,         0,
    0.6275,    0.7529,         0,
    0.1255,    0.2510,    0.5020,
    0.6275,    0.2510,    0.5020,
    0.1255,    0.7529,    0.5020,
    0.6275,    0.7529,    0.5020,
    0.3765,    0.2510,         0,
    0.8784,    0.2510,         0,
    0.3765,    0.7529,         0,
    0.8784,    0.7529,         0,
    0.3765,    0.2510,    0.5020,
    0.8784,    0.2510,    0.5020,
    0.3765,    0.7529,    0.5020,
    0.8784,    0.7529,    0.5020,
    0.1255,         0,    0.2510,
    0.6275,         0,    0.2510,
    0.1255,    0.5020,    0.2510,
    0.6275,    0.5020,    0.2510,
    0.1255,         0,    0.7529,
    0.6275,         0,    0.7529,
    0.1255,    0.5020,    0.7529,
    0.6275,    0.5020,    0.7529,
    0.3765,         0,    0.2510,
    0.8784,         0,    0.2510,
    0.3765,    0.5020,    0.2510,
    0.8784,    0.5020,    0.2510,
    0.3765,         0,    0.7529,
    0.8784,         0,    0.7529,
    0.3765,    0.5020,    0.7529,
    0.8784,    0.5020,    0.7529,
    0.1255,    0.2510,    0.2510,
    0.6275,    0.2510,    0.2510,
    0.1255,    0.7529,    0.2510,
    0.6275,    0.7529,    0.2510,
    0.1255,    0.2510,    0.7529,
    0.6275,    0.2510,    0.7529,
    0.1255,    0.7529,    0.7529,
    0.6275,    0.7529,    0.7529,
    0.3765,    0.2510,    0.2510,
    0.8784,    0.2510,    0.2510,
    0.3765,    0.7529,    0.2510,
    0.8784,    0.7529,    0.2510,
    0.3765,    0.2510,    0.7529,
    0.8784,    0.2510,    0.7529,
    0.3765,    0.7529,    0.7529,
    0.8784,    0.7529,    0.7529,
         0,    0.1255,         0,
    0.5020,    0.1255,         0,
         0,    0.6275,         0,
    0.5020,    0.6275,         0,
         0,    0.1255,    0.5020,
    0.5020,    0.1255,    0.5020,
         0,    0.6275,    0.5020,
    0.5020,    0.6275,    0.5020,
    0.2510,    0.1255,         0,
    0.7529,    0.1255,         0,
    0.2510,    0.6275,         0,
    0.7529,    0.6275,         0,
    0.2510,    0.1255,    0.5020,
    0.7529,    0.1255,    0.5020,
    0.2510,    0.6275,    0.5020,
    0.7529,    0.6275,    0.5020,
         0,    0.3765,         0,
    0.5020,    0.3765,         0,
         0,    0.8784,         0,
    0.5020,    0.8784,         0,
         0,    0.3765,    0.5020,
    0.5020,    0.3765,    0.5020,
         0,    0.8784,    0.5020,
    0.5020,    0.8784,    0.5020,
    0.2510,    0.3765,         0,
    0.7529,    0.3765,         0,
    0.2510,    0.8784,         0,
    0.7529,    0.8784,         0,
    0.2510,    0.3765,    0.5020,
    0.7529,    0.3765,    0.5020,
    0.2510,    0.8784,    0.5020,
    0.7529,    0.8784,    0.5020,
         0,    0.1255,    0.2510,
    0.5020,    0.1255,    0.2510,
         0,    0.6275,    0.2510,
    0.5020,    0.6275,    0.2510,
         0,    0.1255,    0.7529,
    0.5020,    0.1255,    0.7529,
         0,    0.6275,    0.7529,
    0.5020,    0.6275,    0.7529,
    0.2510,    0.1255,    0.2510,
    0.7529,    0.1255,    0.2510,
    0.2510,    0.6275,    0.2510,
    0.7529,    0.6275,    0.2510,
    0.2510,    0.1255,    0.7529,
    0.7529,    0.1255,    0.7529,
    0.2510,    0.6275,    0.7529,
    0.7529,    0.6275,    0.7529,
         0,    0.3765,    0.2510,
    0.5020,    0.3765,    0.2510,
         0,    0.8784,    0.2510,
    0.5020,    0.8784,    0.2510,
         0,    0.3765,    0.7529,
    0.5020,    0.3765,    0.7529,
         0,    0.8784,    0.7529,
    0.5020,    0.8784,    0.7529,
    0.2510,    0.3765,    0.2510,
    0.7529,    0.3765,    0.2510,
    0.2510,    0.8784,    0.2510,
    0.7529,    0.8784,    0.2510,
    0.2510,    0.3765,    0.7529,
    0.7529,    0.3765,    0.7529,
    0.2510,    0.8784,    0.7529,
    0.7529,    0.8784,    0.7529,
    0.1255,    0.1255,         0,
    0.6275,    0.1255,         0,
    0.1255,    0.6275,         0,
    0.6275,    0.6275,         0,
    0.1255,    0.1255,    0.5020,
    0.6275,    0.1255,    0.5020,
    0.1255,    0.6275,    0.5020,
    0.6275,    0.6275,    0.5020,
    0.3765,    0.1255,         0,
    0.8784,    0.1255,         0,
    0.3765,    0.6275,         0,
    0.8784,    0.6275,         0,
    0.3765,    0.1255,    0.5020,
    0.8784,    0.1255,    0.5020,
    0.3765,    0.6275,    0.5020,
    0.8784,    0.6275,    0.5020,
    0.1255,    0.3765,         0,
    0.6275,    0.3765,         0,
    0.1255,    0.8784,         0,
    0.6275,    0.8784,         0,
    0.1255,    0.3765,    0.5020,
    0.6275,    0.3765,    0.5020,
    0.1255,    0.8784,    0.5020,
    0.6275,    0.8784,    0.5020,
    0.3765,    0.3765,         0,
    0.8784,    0.3765,         0,
    0.3765,    0.8784,         0,
    0.8784,    0.8784,         0,
    0.3765,    0.3765,    0.5020,
    0.8784,    0.3765,    0.5020,
    0.3765,    0.8784,    0.5020,
    0.8784,    0.8784,    0.5020,
    0.1255,    0.1255,    0.2510,
    0.6275,    0.1255,    0.2510,
    0.1255,    0.6275,    0.2510,
    0.6275,    0.6275,    0.2510,
    0.1255,    0.1255,    0.7529,
    0.6275,    0.1255,    0.7529,
    0.1255,    0.6275,    0.7529,
    0.6275,    0.6275,    0.7529,
    0.3765,    0.1255,    0.2510,
    0.8784,    0.1255,    0.2510,
    0.3765,    0.6275,    0.2510,
    0.8784,    0.6275,    0.2510,
    0.3765,    0.1255,    0.7529,
    0.8784,    0.1255,    0.7529,
    0.3765,    0.6275,    0.7529,
    0.8784,    0.6275,    0.7529,
    0.1255,    0.3765,    0.2510,
    0.6275,    0.3765,    0.2510,
    0.1255,    0.8784,    0.2510,
    0.6275,    0.8784,    0.2510,
    0.1255,    0.3765,    0.7529,
    0.6275,    0.3765,    0.7529,
    0.1255,    0.8784,    0.7529,
    0.6275,    0.8784,    0.7529,
    0.3765,    0.3765,    0.2510,
    0.8784,    0.3765,    0.2510,
    0.3765,    0.8784,    0.2510,
    0.8784,    0.8784,    0.2510,
    0.3765,    0.3765,    0.7529,
    0.8784,    0.3765,    0.7529,
    0.3765,    0.8784,    0.7529,
    0.8784,    0.8784,    0.7529]


def save_with_pascal_colormap(filename, arr):
  colmap = (np.array(pascal_colormap) * 255).round().astype("uint8")
  palimage = Image.new('P', (16, 16))
  palimage.putpalette(colmap)
  im = Image.fromarray(np.squeeze(arr.astype("uint8")))
  im2 = im.quantize(palette=palimage)
  im2.save(filename)
