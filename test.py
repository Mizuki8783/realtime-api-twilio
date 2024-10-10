import requests


def send_incoming_call_request():
    url = "http://localhost:5050/incoming-call"
    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Request sent successfully.")
        print("Response:", response.text)
    else:
        print("Failed to send request. Status code:", response.status_code)
        print("Response:", response.text)

# Example usage
send_incoming_call_request()
