from flask import Flask, request, redirect
import requests
import base64
import webbrowser

app = Flask(__name__)

CLIENT_ID = '1494184'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:5000/oauth/callback'


@app.route('/')
def home():
    return redirect(
        f"https://www.pinterest.com/oauth/?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"response_type=code&"
        f"scope=boards:read,pins:read"
    )


@app.route('/oauth/callback')
def pinterest_oauth_callback():
    code = request.args.get('code')
    state = request.args.get('state')
    access_token = exchange_code_for_token(code)
    # Vous pouvez maintenant utiliser le token d'accès
    return 'Token d\'accès obtenu: ' + access_token


def exchange_code_for_token(code):
    url = 'https://api.pinterest.com/v5/oauth/token'
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    credentials_b64 = base64.b64encode(credentials.encode()).decode()

    headers = {
        'Authorization': f'Basic {credentials_b64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception('Échec de l\'obtention du token d\'accès')


def get_access_token():
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)
