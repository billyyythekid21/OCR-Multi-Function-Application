import pytesseract
from PIL import Image

# Specify the path to the Tesseract executable (usually not needed on macOS if installed via Homebrew)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def ocr_image(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
    return text

# Settings
image_path = 'test.png'
extracted_text = ocr_image(image_path)
print(extracted_text)
