import pytesseract
from PIL import Image

# Set the path to Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def text_recognition(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Example usage
image_path = 'path/to/your/image.png'
result = text_recognition(image_path)
print("Text Recognition Result:")
print(result)
