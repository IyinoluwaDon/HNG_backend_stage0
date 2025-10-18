\# Backend Stage 0 - Dynamic Profile Endpoint



\[!\[Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

\[!\[Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)

\[!\[License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)



A RESTful API endpoint that returns my profile information along with a dynamically fetched cat fact from an external API. Built as part of the HNG Backend Internship - Stage 0.



\## 📋 Table of Contents

\# Backend Stage 0 - Dynamic Profile Endpoint



\[!\[Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

\[!\[Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)

\[!\[License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)



A RESTful API endpoint that returns my profile information along with a dynamically fetched cat fact from an external API. Built as part of the HNG Backend Internship - Stage 0.



\## 📋 Table of Contents



\- \[Description](#description)

\- \[Features](#features)

\- \[Tech Stack](#tech-stack)

\- \[Live Demo](#live-demo)

\- \[Installation](#installation)

\- \[Running Locally](#running-locally)

\- \[API Documentation](#api-documentation)

\- \[Project Structure](#project-structure)

\- \[Deployment](#deployment)

\- \[Author](#author)



\## 📖 Description



This project implements a simple yet dynamic API endpoint (`/me`) that demonstrates:

\- RESTful API design principles

\- Integration with third-party APIs

\- Proper error handling and fallback mechanisms

\- JSON response formatting

\- CORS configuration for cross-origin requests



\## ✨ Features



\- ✅ Returns profile information in JSON format

\- ✅ Fetches random cat facts from external API on every request

\- ✅ Dynamic UTC timestamp in ISO 8601 format

\- ✅ Graceful error handling with fallback cat fact

\- ✅ CORS enabled for cross-origin requests

\- ✅ Clean, well-documented code



\## 🛠️ Tech Stack



\- \*\*Language:\*\* Python 3.12

\- \*\*Framework:\*\* Flask 3.0.0

\- \*\*HTTP Client:\*\* Requests 2.31.0

\- \*\*CORS:\*\* Flask-CORS 4.0.0



\## 🚀 Live Demo



\*\*Live API Endpoint:\*\* `https://your-deployment-url.up.railway.app/me`  

\*(Update this after deployment)\*



Try it out:

```bash

curl https://your-deployment-url.up.railway.app/me

```



\## 📦 Installation



\### Prerequisites

\- Python 3.8 or higher

\- pip (Python package manager)

\- Git



\### Steps



1\. \*\*Clone the repository\*\*

&nbsp;  ```bash

&nbsp;  git clone https://github.com/YOUR\_GITHUB\_USERNAME/backend-stage0.git

&nbsp;  cd backend-stage0

&nbsp;  ```



2\. \*\*Create a virtual environment (recommended)\*\*

&nbsp;  ```bash

&nbsp;  # Windows

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate



&nbsp;  # macOS/Linux

&nbsp;  python3 -m venv venv

&nbsp;  source venv/bin/activate

&nbsp;  ```



3\. \*\*Install dependencies\*\*

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

&nbsp;  ```



\## 💻 Running Locally



1\. \*\*Start the Flask server\*\*

&nbsp;  ```bash

&nbsp;  python backend\_stage0.py

&nbsp;  ```



2\. \*\*Access the API\*\*

&nbsp;  - Open your browser and navigate to: `http://localhost:5000/me`

&nbsp;  - Or use curl: `curl http://localhost:5000/me`



3\. \*\*Expected output\*\*

&nbsp;  ```json

&nbsp;  {

&nbsp;    "status": "success",

&nbsp;    "user": {

&nbsp;      "email": "iyinoluwadontaiwo@gmail.com",

&nbsp;      "name": "Iyinoluwa Don-Taiwo",

&nbsp;      "stack": "Python/Flask"

&nbsp;    },

&nbsp;    "timestamp": "2025-10-18T14:30:45.789Z",

&nbsp;    "fact": "Cats sleep for 70% of their lives."

&nbsp;  }

&nbsp;  ```



\## 📡 API Documentation



\### Endpoint: `GET /me`



Returns user profile information along with a random cat fact.



\#### Request

```http

GET /me HTTP/1.1

Host: your-api-domain.com

```



\#### Response



\*\*Success Response (200 OK)\*\*

```json

{

&nbsp; "status": "success",

&nbsp; "user": {

&nbsp;   "email": "string",

&nbsp;   "name": "string",

&nbsp;   "stack": "string"

&nbsp; },

&nbsp; "timestamp": "string (ISO 8601 format)",

&nbsp; "fact": "string"

}

```



\*\*Error Response (500 Internal Server Error)\*\*

```json

{

&nbsp; "status": "error",

&nbsp; "message": "An unexpected error occurred",

&nbsp; "error": "string"

}

```



\#### Response Fields



| Field | Type | Description |

|-------|------|-------------|

| `status` | string | Always "success" for successful requests |

| `user.email` | string | Personal email address |

| `user.name` | string | Full name |

| `user.stack` | string | Backend technology stack |

| `timestamp` | string | Current UTC time in ISO 8601 format |

| `fact` | string | Random cat fact from Cat Facts API |



\#### Example Request



\*\*Using curl:\*\*

```bash

curl -X GET https://your-api-domain.com/me

```



\*\*Using Python:\*\*

```python

import requests



response = requests.get('https://your-api-domain.com/me')

data = response.json()

print(data)

```



\*\*Using JavaScript:\*\*

```javascript

fetch('https://your-api-domain.com/me')

&nbsp; .then(response => response.json())

&nbsp; .then(data => console.log(data));

```



\## 📁 Project Structure



```

backend-stage0/

│

├── backend\_stage0.py      # Main Flask application

├── requirements.txt       # Python dependencies

├── README.md             # Project documentation

├── .gitignore            # Git ignore rules

└── Procfile              # Deployment configuration (if using Heroku)

```



\## 🌐 Deployment



This project is deployed on \*\*Railway\*\* (or your chosen platform).



\### Deployment Steps



1\. \*\*Push to GitHub\*\*

&nbsp;  ```bash

&nbsp;  git add .

&nbsp;  git commit -m "Ready for deployment"

&nbsp;  git push origin main

&nbsp;  ```



2\. \*\*Deploy on Railway\*\*

&nbsp;  - Go to \[Railway.app](https://railway.app)

&nbsp;  - Connect your GitHub repository

&nbsp;  - Railway will automatically detect Python and deploy

&nbsp;  - Your API will be live at the provided URL



3\. \*\*Environment Configuration\*\*

&nbsp;  - No environment variables required for this project

&nbsp;  - Port is automatically configured by the hosting platform



\### Verify Deployment



Test your deployed endpoint:

```bash

curl https://your-deployment-url.up.railway.app/me

```



\## 📋 Dependencies



All dependencies are listed in `requirements.txt`:



```

Flask==3.0.0

requests==2.31.0

flask-cors==4.0.0

```



\### Why These Dependencies?



\- \*\*Flask\*\*: Lightweight web framework for building the API

\- \*\*requests\*\*: HTTP library for fetching cat facts from external API

\- \*\*flask-cors\*\*: Enables Cross-Origin Resource Sharing (CORS)



\## 🧪 Testing



\### Manual Testing



1\. \*\*Test locally:\*\*

&nbsp;  ```bash

&nbsp;  python backend\_stage0.py

&nbsp;  curl http://localhost:5000/me

&nbsp;  ```



2\. \*\*Test timestamp updates:\*\*

&nbsp;  ```bash

&nbsp;  # Make multiple requests and verify timestamp changes

&nbsp;  curl http://localhost:5000/me | jq '.timestamp'

&nbsp;  curl http://localhost:5000/me | jq '.timestamp'

&nbsp;  ```



3\. \*\*Test cat fact changes:\*\*

&nbsp;  ```bash

&nbsp;  # Verify different cat facts on each request

&nbsp;  curl http://localhost:5000/me | jq '.fact'

&nbsp;  curl http://localhost:5000/me | jq '.fact'

&nbsp;  ```



\### Error Handling



The API includes graceful error handling:

\- If the Cat Facts API is down, a fallback fact is provided

\- Timeout is set to 5 seconds to prevent hanging

\- All errors return proper HTTP status codes



\## 🤝 Contributing



This is a personal internship project, but feedback is welcome!



\## 👤 Author



\*\*Iyinoluwa Don-Taiwo\*\*



\- Email: iyinoluwadontaiwo@gmail.com

\- GitHub: \[@YOUR\_GITHUB\_USERNAME](https://github.com/YOUR\_GITHUB\_USERNAME)

\- LinkedIn: \[Your LinkedIn Profile](https://linkedin.com/in/YOUR\_LINKEDIN) \*(optional - remove if you don't have one)\*



\## 📄 License



This project is licensed under the MIT License - see the \[LICENSE](LICENSE) file for details.



\## 🙏 Acknowledgments



\- \[HNG Internship](https://hng.tech) for the opportunity

\- \[Cat Facts API](https://catfact.ninja) for providing the cat facts

\- Flask community for excellent documentation



\## 📝 Task Details



This project was completed as part of:

\- \*\*Program:\*\* HNG Backend Internship

\- \*\*Stage:\*\* Stage 0

\- \*\*Task:\*\* Build a Dynamic Profile Endpoint

\- \*\*Deadline:\*\* Sunday, October 19, 2025



---



⭐ If you found this project interesting, please consider giving it a star on GitHub!



\*\*Built with ❤️ as part of the HNG Internship Backend Track\*\*

\- \[Description](#description)

\- \[Features](#features)

\- \[Tech Stack](#tech-stack)

\- \[Live Demo](#live-demo)

\- \[Installation](#installation)

\- \[Running Locally](#running-locally)

\- \[API Documentation](#api-documentation)

\- \[Project Structure](#project-structure)

\- \[Deployment](#deployment)

\- \[Author](#author)



\## 📖 Description



This project implements a simple yet dynamic API endpoint (`/me`) that demonstrates:

\- RESTful API design principles

\- Integration with third-party APIs

\- Proper error handling and fallback mechanisms

\- JSON response formatting

\- CORS configuration for cross-origin requests



\## ✨ Features



\- ✅ Returns profile information in JSON format

\- ✅ Fetches random cat facts from external API on every request

\- ✅ Dynamic UTC timestamp in ISO 8601 format

\- ✅ Graceful error handling with fallback cat fact

\- ✅ CORS enabled for cross-origin requests

\- ✅ Clean, well-documented code



\## 🛠️ Tech Stack



\- \*\*Language:\*\* Python 3.12

\- \*\*Framework:\*\* Flask 3.0.0

\- \*\*HTTP Client:\*\* Requests 2.31.0

\- \*\*CORS:\*\* Flask-CORS 4.0.0



\## 🚀 Live Demo



\*\*Live API Endpoint:\*\* `https://your-deployment-url.up.railway.app/me`  

\*(Update this after deployment)\*



Try it out:

```bash

curl https://your-deployment-url.up.railway.app/me

```



\## 📦 Installation



\### Prerequisites

\- Python 3.8 or higher

\- pip (Python package manager)

\- Git



\### Steps



1\. \*\*Clone the repository\*\*

&nbsp;  ```bash

&nbsp;  git clone https://github.com/YOUR\_GITHUB\_USERNAME/backend-stage0.git

&nbsp;  cd backend-stage0

&nbsp;  ```



2\. \*\*Create a virtual environment (recommended)\*\*

&nbsp;  ```bash

&nbsp;  # Windows

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate



&nbsp;  # macOS/Linux

&nbsp;  python3 -m venv venv

&nbsp;  source venv/bin/activate

&nbsp;  ```



3\. \*\*Install dependencies\*\*

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

&nbsp;  ```



\## 💻 Running Locally



1\. \*\*Start the Flask server\*\*

&nbsp;  ```bash

&nbsp;  python backend\_stage0.py

&nbsp;  ```



2\. \*\*Access the API\*\*

&nbsp;  - Open your browser and navigate to: `http://localhost:5000/me`

&nbsp;  - Or use curl: `curl http://localhost:5000/me`



3\. \*\*Expected output\*\*

&nbsp;  ```json

&nbsp;  {

&nbsp;    "status": "success",

&nbsp;    "user": {

&nbsp;      "email": "iyinoluwadontaiwo@gmail.com",

&nbsp;      "name": "Iyinoluwa Don-Taiwo",

&nbsp;      "stack": "Python/Flask"

&nbsp;    },

&nbsp;    "timestamp": "2025-10-18T14:30:45.789Z",

&nbsp;    "fact": "Cats sleep for 70% of their lives."

&nbsp;  }

&nbsp;  ```



\## 📡 API Documentation



\### Endpoint: `GET /me`



Returns user profile information along with a random cat fact.



\#### Request

```http

GET /me HTTP/1.1

Host: your-api-domain.com

```



\#### Response



\*\*Success Response (200 OK)\*\*

```json

{

&nbsp; "status": "success",

&nbsp; "user": {

&nbsp;   "email": "string",

&nbsp;   "name": "string",

&nbsp;   "stack": "string"

&nbsp; },

&nbsp; "timestamp": "string (ISO 8601 format)",

&nbsp; "fact": "string"

}

```



\*\*Error Response (500 Internal Server Error)\*\*

```json

{

&nbsp; "status": "error",

&nbsp; "message": "An unexpected error occurred",

&nbsp; "error": "string"

}

```



\#### Response Fields



| Field | Type | Description |

|-------|------|-------------|

| `status` | string | Always "success" for successful requests |

| `user.email` | string | Personal email address |

| `user.name` | string | Full name |

| `user.stack` | string | Backend technology stack |

| `timestamp` | string | Current UTC time in ISO 8601 format |

| `fact` | string | Random cat fact from Cat Facts API |



\#### Example Request



\*\*Using curl:\*\*

```bash

curl -X GET https://your-api-domain.com/me

```



\*\*Using Python:\*\*

```python

import requests



response = requests.get('https://your-api-domain.com/me')

data = response.json()

print(data)

```



\*\*Using JavaScript:\*\*

```javascript

fetch('https://your-api-domain.com/me')

&nbsp; .then(response => response.json())

&nbsp; .then(data => console.log(data));

```



\## 📁 Project Structure



```

backend-stage0/

│

├── backend\_stage0.py      # Main Flask application

├── requirements.txt       # Python dependencies

├── README.md             # Project documentation

├── .gitignore            # Git ignore rules

└── Procfile              # Deployment configuration (if using Heroku)

```



\## 🌐 Deployment



This project is deployed on \*\*Railway\*\* (or your chosen platform).



\### Deployment Steps



1\. \*\*Push to GitHub\*\*

&nbsp;  ```bash

&nbsp;  git add .

&nbsp;  git commit -m "Ready for deployment"

&nbsp;  git push origin main

&nbsp;  ```



2\. \*\*Deploy on Railway\*\*

&nbsp;  - Go to \[Railway.app](https://railway.app)

&nbsp;  - Connect your GitHub repository

&nbsp;  - Railway will automatically detect Python and deploy

&nbsp;  - Your API will be live at the provided URL



3\. \*\*Environment Configuration\*\*

&nbsp;  - No environment variables required for this project

&nbsp;  - Port is automatically configured by the hosting platform



\### Verify Deployment



Test your deployed endpoint:

```bash

curl https://your-deployment-url.up.railway.app/me

```



\## 📋 Dependencies



All dependencies are listed in `requirements.txt`:



```

Flask==3.0.0

requests==2.31.0

flask-cors==4.0.0

```



\### Why These Dependencies?



\- \*\*Flask\*\*: Lightweight web framework for building the API

\- \*\*requests\*\*: HTTP library for fetching cat facts from external API

\- \*\*flask-cors\*\*: Enables Cross-Origin Resource Sharing (CORS)



\## 🧪 Testing



\### Manual Testing



1\. \*\*Test locally:\*\*

&nbsp;  ```bash

&nbsp;  python backend\_stage0.py

&nbsp;  curl http://localhost:5000/me

&nbsp;  ```



2\. \*\*Test timestamp updates:\*\*

&nbsp;  ```bash

&nbsp;  # Make multiple requests and verify timestamp changes

&nbsp;  curl http://localhost:5000/me | jq '.timestamp'

&nbsp;  curl http://localhost:5000/me | jq '.timestamp'

&nbsp;  ```



3\. \*\*Test cat fact changes:\*\*

&nbsp;  ```bash

&nbsp;  # Verify different cat facts on each request

&nbsp;  curl http://localhost:5000/me | jq '.fact'

&nbsp;  curl http://localhost:5000/me | jq '.fact'

&nbsp;  ```



\### Error Handling



The API includes graceful error handling:

\- If the Cat Facts API is down, a fallback fact is provided

\- Timeout is set to 5 seconds to prevent hanging

\- All errors return proper HTTP status codes



\## 🤝 Contributing



This is a personal internship project, but feedback is welcome!



\## 👤 Author



\*\*Iyinoluwa Don-Taiwo\*\*



\- Email: iyinoluwadontaiwo@gmail.com

\- GitHub: \[@YOUR\_GITHUB\_USERNAME](https://github.com/YOUR\_GITHUB\_USERNAME)

\- LinkedIn: \[Your LinkedIn Profile](https://linkedin.com/in/YOUR\_LINKEDIN) \*(optional - remove if you don't have one)\*



\## 📄 License



This project is licensed under the MIT License - see the \[LICENSE](LICENSE) file for details.



\## 🙏 Acknowledgments



\- \[HNG Internship](https://hng.tech) for the opportunity

\- \[Cat Facts API](https://catfact.ninja) for providing the cat facts

\- Flask community for excellent documentation



\## 📝 Task Details



This project was completed as part of:

\- \*\*Program:\*\* HNG Backend Internship

\- \*\*Stage:\*\* Stage 0

\- \*\*Task:\*\* Build a Dynamic Profile Endpoint

\- \*\*Deadline:\*\* Sunday, October 19, 2025



---



⭐ If you found this project interesting, please consider giving it a star on GitHub!



\*\*Built with ❤️ as part of the HNG Internship Backend Track\*\*

