import requests
from PIL import Image, ImageDraw, ImageFont
import io

def create_test_image():
    """Create a simple test image with Japanese text"""
    img = Image.new('RGB', (300, 100), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw some text (will be in default font, but good enough for testing)
    draw.text((50, 30), "Hello こんにちは", fill='black')
    
    # Save to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    return img_bytes

def test_ocr_endpoint():
    """Test the OCR endpoint"""
    url = "http://localhost:8000/ocr"
    
    # Create test image
    img_bytes = create_test_image()
    
    # Send request
    files = {'file': ('test.png', img_bytes, 'image/png')}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Status: {result['status']}")
        print(f"Extracted text: {result['text']}")
        print(f"Filename: {result['filename']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    print("Testing OCR endpoint...")
    print("Make sure the server is running with: python main.py")
    print("-" * 50)
    
    try:
        test_ocr_endpoint()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server. Make sure it's running on http://localhost:8000")