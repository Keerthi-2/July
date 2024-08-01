import requests
import getAuth
token_url="https://www.linkedin.com/oauth/v2/accessToken"

authorization_code=getAuth()
token_params = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(token_url, data=token_params)
access_token = response.json().get('access_token')

print("Access Token:", access_token)