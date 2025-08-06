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
    app.run(debug=True)


import msal

client_id = "5de4ce05-f6be-47dc-a56b-ee71cd503b8f"
client_secret = "d4e81cda-f325-4cea-a0b5-2fefb4e90eff"
tenant_id = "f38a5ecd-2813-4862-b11b-ac1d563c806f"

authority = f"https://login.microsoftonline.com/{tenant_id}"
app = msal.ConfidentialClientApplication(
    client_id, authority=authority, client_credential=client_secret
)

token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
