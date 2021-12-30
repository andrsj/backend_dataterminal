import requests


from api.config import CLIENT_ID, CLIENT_SECRET, API_ENDPOINT


def exchange_code(code: str, redirect_uri: str):
    """Getting user credentials via Discord API by application"""
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(
        f'{API_ENDPOINT}/oauth2/token',
        data=data,
        headers=headers
    )

    r.raise_for_status()
    return r.json()


def get_current_authorization_information(token: str):
    """Getting application and user authorization information"""
    r = requests.get(
        f'{API_ENDPOINT}/oauth2/@me',
        headers={
            'Authorization': f'Bearer {token}'
        }
    )

    r.raise_for_status()
    return r.json()
