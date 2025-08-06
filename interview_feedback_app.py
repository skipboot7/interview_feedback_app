from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/interview-feedback')
def get_feedback():
    with open('mock_feedback.json') as f:
        data = json.load(f)
    filtered = [entry for entry in data if entry['location'] == 'Boise' and 'Firmware' in entry['job_title']]
    return jsonify(filtered)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
