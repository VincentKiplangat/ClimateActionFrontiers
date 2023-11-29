import json
from base64 import b64encode
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

from ClimateActionFrontier_EmobilisProjectShowcasing import settings


def get_access_token():
    url = settings.MPESA_API["CREDENTIALS_URL"]
    consumer_key = settings.MPESA_API["CONSUMER_KEY"]
    consumer_secret = settings.MPESA_API["CONSUMER_SECRET"]
    auth = HTTPBasicAuth(consumer_key, consumer_secret)
    try:
        response = requests.get(url, auth=auth)
    except Exception as err:
        raise err
    else:
        token = response.json()["access_token"]
        return token


def generate_password():
    timestamp = get_current_timestamp()
    biz_short_code = get_business_shortcode()
    passkey = settings.MPESA_API["PASS_KEY"]
    password_string = biz_short_code + passkey + timestamp
    encoded_bytes = password_string.encode("ascii")
    password = b64encode(encoded_bytes).decode("utf-8")
    return password


def get_current_timestamp():
    return datetime.now().strftime('%Y%m%d%H%M%S')


def generate_request_headers():
    token = get_access_token()
    return {"Authorization": f"Bearer {token}"}


def get_business_shortcode():
    return settings.MPESA_API["BIZ_SHORT_CODE"]


def get_payment_url():
    return settings.MPESA_API["PAYMENT_URL"]


def get_callback_url():
    return settings.MPESA_API["CALLBACK_URL"]


