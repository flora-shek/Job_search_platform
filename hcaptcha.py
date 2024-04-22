import os
import requests

site_key = os.environ['site_key']
secret_key = os.environ['site_secret']
VERIFY_URL = "https://api.hcaptcha.com/siteverify"

def verify_hcaptcha(token):
  data = { 'secret': secret_key, 'response': token }
  response = requests.post(url=VERIFY_URL, data=data)
  response_json = response.json()
  success = response_json['success']
  return success