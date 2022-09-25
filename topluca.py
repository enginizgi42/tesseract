import skimage.io as sio
import skimage

import pytesseract
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray

for x in range(3):
    image=sio.imread(r'C:\Users\Engin\Desktop\uygulamalar\tesseract\{}.jpg'.format(x))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    image=rgb2gray(image)
    otsu=threshold_otsu(image)
    imagebinari=image>otsu
    text=pytesseract.image_to_string(imagebinari,lang="tur")#eng
    print(text)
