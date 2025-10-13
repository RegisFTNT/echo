# Echo - HTTP Method Echo Server

A lightweight Python HTTP server that echoes back the HTTP method used in requests. Perfect for testing, debugging, and understanding HTTP request methods.

## Overview

Echo is a simple HTTP server built with Python's standard library that responds with the HTTP method used in each request (GET, POST, PUT, DELETE, PATCH, etc.). It's an invaluable tool for:

- Testing REST API clients
- Learning about HTTP methods
- Debugging HTTP requests
- Validating request method handling
- Teaching HTTP fundamentals
- Integration testing with mock endpoints

## Features

- **Method Echo**: Returns clear confirmation of the HTTP method used
- **Lightweight**: Uses only Python's standard library - no external dependencies
- **Logging**: Built-in request logging to track all incoming requests
- **Docker Support**: Includes Dockerfile for easy containerization
- **Comprehensive**: Supports GET, POST, PUT, DELETE, PATCH, HEAD, and OPTIONS methods
- **Simple**: Minimal setup, just run and test

## Requirements

- Python 3.12+ (or Python 3.x)
- No external dependencies required

## Installation

### Clone the Repository

```bash
git clone https://github.com/regisftm/echo.git
cd echo
```

## Usage

### Running Locally

#### Option 1: Direct Python Execution

```bash
cd app
python app.py
```

The server will start on port 80 by default. If you need to run on a different port, you can modify the `port` parameter in `app.py`.

#### Option 2: Run on a Different Port (requires code modification)

Edit `app/app.py` and change the last line:

```python
if __name__ == '__main__':
    run(port=8080)  # Change 80 to your desired port
```

### Running with Docker

#### Build the Docker Image

```bash
docker build -t echo-server .
```

#### Run the Container

```bash
docker run -p 8080:80 echo-server
```

This maps port 80 inside the container to port 8080 on your host machine.

## Testing the Server

### Using cURL

```bash
# GET request
curl http://localhost:80/
# Response: Request HTTP Method: GET

# POST request
curl -X POST http://localhost:80/
# Response: Request HTTP Method: POST

# PUT request
curl -X PUT http://localhost:80/
# Response: Request HTTP Method: PUT

# DELETE request
curl -X DELETE http://localhost:80/
# Response: Request HTTP Method: DELETE

# PATCH request
curl -X PATCH http://localhost:80/
# Response: Request HTTP Method: PATCH

# HEAD request (no body returned)
curl -I http://localhost:80/

# OPTIONS request (shows allowed methods)
curl -X OPTIONS http://localhost:80/
```

### Using HTTPie

```bash
# GET request
http GET localhost:80

# POST request
http POST localhost:80

# PUT request
http PUT localhost:80
```

### Using Python Requests

```python
import requests

# GET request
response = requests.get('http://localhost:80')
print(response.text)  # Output: Request HTTP Method: GET

# POST request
response = requests.post('http://localhost:80')
print(response.text)  # Output: Request HTTP Method: POST

# PUT request
response = requests.put('http://localhost:80')
print(response.text)  # Output: Request HTTP Method: PUT
```

### Using JavaScript/Fetch API

```javascript
// GET request
fetch('http://localhost:80')
  .then(response => response.text())
  .then(data => console.log(data));
  // Output: Request HTTP Method: GET

// POST request
fetch('http://localhost:80', {
  method: 'POST'
})
  .then(response => response.text())
  .then(data => console.log(data));
  // Output: Request HTTP Method: POST
```

## How It Works

The server is built using Python's `http.server` module and implements handlers for common HTTP methods:

- **GET**: Returns "Request HTTP Method: GET"
- **POST**: Returns "Request HTTP Method: POST"
- **PUT**: Returns "Request HTTP Method: PUT"
- **DELETE**: Returns "Request HTTP Method: DELETE"
- **PATCH**: Returns "Request HTTP Method: PATCH"
- **HEAD**: Returns headers only (no body)
- **OPTIONS**: Returns allowed methods in the Allow header

All requests are logged with timestamps for debugging purposes.

## Use Cases

### 1. Testing REST API Clients

Quickly verify that your HTTP client is sending the correct methods without needing a full backend.

### 2. Learning Tool

Great for teaching and learning about HTTP methods and how they work in practice.

### 3. Integration Testing

Use as a mock endpoint in your integration tests to verify HTTP method handling.

### 4. Debugging

Confirm what HTTP method your application is actually sending when troubleshooting issues.

### 5. CI/CD Testing

Deploy in containers for automated testing of API clients in your CI/CD pipeline.

## Configuration

The server configuration is straightforward:

- **Port**: Default is 80 (can be changed in `app.py`)
- **Host**: Listens on all interfaces (0.0.0.0)
- **Logging**: INFO level by default

## Docker Deployment

The included Dockerfile uses Python 3.12.1-slim as the base image and exposes port 80. To deploy:

```bash
# Build
docker build -t echo-server .

# Run with custom port mapping
docker run -d -p 3000:80 --name my-echo-server echo-server

# Check logs
docker logs my-echo-server

# Stop
docker stop my-echo-server
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source. Please check the repository for specific license information.

## Author

[regisftm](https://github.com/regisftm)

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/regisftm/echo/issues) on GitHub.

---

[!Note]: This is a development/testing tool. It's not intended for production use without proper security considerations and enhancements.
