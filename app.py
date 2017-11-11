from flask import Flask
from flask import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/campsites')
def index():
    data = get_campsites()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

def get_campsites():
    data = [{
        'latitude': '39.2030556',
        'longitude': '-123.1863889',
        'facilityName': 'CHEKAKA RECREATION AREA LAKE MENDOCINO'
        },
        {
        'latitude': '37.9844444',
        'longitude': '-120.8447222',
        'facilityName': 'COYOTE POINT'
        }]
    return data

if __name__ == '__main__':
    app.run()
