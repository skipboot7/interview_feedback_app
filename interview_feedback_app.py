from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/interview-feedback')
def get_feedback():
    with open('mock_feedback.json') as f:
        data = json.load(f)
    filtered = [entry for entry in data if entry['location'] == 'Boise' and 'Firmware' in entry['job_title']]
    return jsonify(filtered)

if __name__ == '__main__':
    # Required for public access on Render
    app.run(host='0.0.0.0', port=10000, debug=True)
