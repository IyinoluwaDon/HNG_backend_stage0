from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

# create the /me endpoint
@app.route('/me', methods=['GET'])
def get_profile():
    """Return user profile information with a random cat fact."""
    try:
        # Fetch cat fact from external API
        try:
            cat_response = requests.get('https://catfact.ninja/fact', timeout=5)
            cat_response.raise_for_status()
            cat_fact = cat_response.json()['fact']
        except:
            cat_fact = "Cats sleep for 70% of their lives."

        # Generate current UTC timestamp in ISO 8601 format
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        # Build response
        response_data = {
            "status": "success",
            "user": {
                "email": "iyinoluwadontaiwo@gmail.com",
                "name": "Iyinoluwa Don-Taiwo",
                "stack": "Python/Flask"
            },
            "timestamp": timestamp,
            "fact": cat_fact
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred",
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)