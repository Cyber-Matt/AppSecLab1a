# ----------
# Matthew Cowell
# ----------

import sys
from PIL import Image

# open the file
file = sys.argv[1]
image = Image.open(file)

# resize with the tuple
newSize = int(sys.argv[3])
newImage = image.resize((newSize, newSize))

# save to the new file name
newImage.save(sys.argv[2])
