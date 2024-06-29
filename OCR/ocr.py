import pytesseract
from PIL import Image

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
    return text

# Example usage
image_path = 'path_to_your_image.png'
extracted_text = ocr_image(image_path)
print(extracted_text)
