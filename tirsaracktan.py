import skimage.io as sio
import skimage

import pytesseract
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
image=sio.imread(r'C:\Users\Engin\Desktop\uygulamalar\tesseract\haci.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
image=rgb2gray(image)
otsu=threshold_otsu(image)
imagebinari=image>otsu
#Tesseract Buradan itibaren kullanılıyor. 
text=pytesseract.image_to_string(imagebinari,lang="tur")#eng
print(text)
