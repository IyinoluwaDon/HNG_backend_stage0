# Backend Stage 0 - Dynamic Profile API

A RESTful API endpoint that returns profile information with a dynamically fetched cat fact from an external API.

**Built for:** HNG Backend Internship - Stage 0  
**Deadline:** October 19, 2025

## 🔗 Live API

**Endpoint:** `https://your-deployment-url.up.railway.app/me`  
*(Update after deployment)*

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Framework:** Flask 3.0.0
- **HTTP Client:** Requests 2.31.0
- **CORS:** Flask-CORS 4.0.0

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/backend-stage0.git
cd backend-stage0
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

The `requirements.txt` contains:
- Flask==3.0.0
- requests==2.31.0
- flask-cors==4.0.0

## 💻 Running Locally

1. **Start the server**
```bash
python backend_stage0.py
```

2. **The server will start on:**
```
http://localhost:5000
```

3. **Access the endpoint:**
```
http://localhost:5000/me
```

## 📡 API Documentation

### Endpoint: `GET /me`

Returns user profile information along with a random cat fact.

## 🧪 Testing the Endpoint

### Using Browser
Simply visit: `http://localhost:5000/me`

### Using curl
```bash
curl http://localhost:5000/me
```

### Using Python
```python
import requests

response = requests.get('http://localhost:5000/me')
print(response.json())
```

The application runs with default configuration:
- Host: `0.0.0.0` (accessible from all network interfaces)
- Port: `5000` (or assigned by deployment platform)
- Debug: `True` for local development

## 🌐 Deployment

Deployed on **Railway** *(or your chosen platform)*

The application automatically adapts to deployment environments by:
- Using the platform-assigned PORT if available
- Binding to `0.0.0.0` for external access
- Disabling debug mode in production

## 📁 Project Structure

```
backend-stage0/
├── backend_stage0.py    # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## 🔧 Dependencies

All dependencies are listed in `requirements.txt`:

```
Flask==3.0.0
requests==2.31.0
flask-cors==4.0.0
```

## 👤 Author

**Iyinoluwa Don-Taiwo**
- **Email:** iyinoluwadontaiwo@gmail.com
- **GitHub:** [@YOUR_USERNAME](https://github.com/DonIyin)
- **Stack:** Python/Flask

- Cat facts are fetched from: `https://catfact.ninja/fact`
