# Fast OCR - Japanese Text Extraction API

A FastAPI-based web service for extracting Japanese text from images using the manga-ocr library.

## Features

- Simple REST API endpoint for Japanese OCR
- Supports common image formats (PNG, JPG, JPEG, etc.)
- Uses the manga-ocr model specialized for Japanese text extraction
- Automatic model loading on startup

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python main.py
```

The server will start on `http://localhost:8000`

2. Send a POST request to `/ocr` with an image file:

```bash
curl -X POST "http://localhost:8000/ocr" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_image.png"
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

- `GET /` - Health check endpoint
- `POST /ocr` - Extract Japanese text from an uploaded image

## Testing

Run the test script:
```bash
python test_endpoint.py
```

## Docker Usage

### Using Docker Compose (Recommended)

1. For development:
```bash
docker-compose up --build
```

2. For production (using pre-built image from GHCR):
```bash
# Copy and edit the environment file
cp .env.example .env
# Edit .env with your GitHub username and repo name

# Run with production config
docker-compose -f docker-compose.prod.yml up -d
```

### Using Docker directly

```bash
# Build the image
docker build -t fast-ocr .

# Run the container
docker run -p 8000:8000 fast-ocr
```

### Using pre-built image from GitHub Container Registry

```bash
docker run -p 8000:8000 ghcr.io/vladimish/fast-ocr:latest
```

## Note

The first run will download the manga-ocr model (~400MB), which may take some time depending on your internet connection. The Docker image has the model pre-downloaded during build.