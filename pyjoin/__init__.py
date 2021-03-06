"""Python API for using Join by joaoapps."""
import requests
import urllib

SEND_URL = "https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?apikey="
LIST_URL = "https://joinjoaomgcd.appspot.com/_ah/api/registration/v1/listDevices?apikey="

def get_devices(api_key):
    response = requests.get(LIST_URL + api_key).json()
    if response.get('success') and not response.get('userAuthError'):
        return [(r['deviceName'], r['deviceId']) for r in response['records']]
    return False

def send_notification(api_key, text, device_id=None, device_ids=None, device_names=None, title=None, icon=None, smallicon=None, vibration=None, image=None):
    if device_id is None and device_ids is None and device_names is None: return False
    req_url = SEND_URL + api_key + "&text=" + text
    if title: req_url += "&title=" + title
    if icon: req_url += "&icon=" + icon
    if image: req_url += "&image=" + urllib.parse.quote(image)
    if smallicon: req_url += "&smallicon=" + smallicon
    if vibration: req_url += "&vibration=" + vibration
    if device_id: req_url += "&deviceId=" + device_id
    if device_ids: req_url += "&deviceIds=" + device_ids
    if device_names: req_url += "&deviceNames=" + device_names
    requests.get(req_url)

def ring_device(api_key, device_id=None, device_ids=None, device_names=None):
    if device_id is None and device_ids is None and device_names is None: return False
    req_url = SEND_URL + api_key + "&find=true"
    if device_id: req_url += "&deviceId=" + device_id
    if device_ids: req_url += "&deviceIds=" + device_ids
    if device_names: req_url += "&deviceNames=" + device_names
    requests.get(req_url)

def send_url(api_key, url, device_id=None, device_ids=None, device_names=None, title=None, text=None):
    if device_id is None and device_ids is None and device_names is None: return False
    req_url = SEND_URL + api_key + "&url=" + url
    if title: req_url += "&title=" + title
    req_url += "&text=" + text if text else "&text="
    if device_id: req_url += "&deviceId=" + device_id
    if device_ids: req_url += "&deviceIds=" + device_ids
    if device_names: req_url += "&deviceNames=" + device_names
    requests.get(req_url)

def set_wallpaper(api_key, url, device_id=None, device_ids=None, device_names=None):
    if device_id is None and device_ids is None and device_names is None: return False
    req_url = SEND_URL + api_key + "&wallpaper=" + url
    if device_id: req_url += "&deviceId=" + device_id
    if device_ids: req_url += "&deviceIds=" + device_ids
    if device_names: req_url += "&deviceNames=" + device_names
    requests.get(req_url)

def send_file(api_key, url, device_id=None, device_ids=None, device_names=None, title=None, text=None):
    if device_id is None and device_ids is None and device_names is None: return False
    req_url = SEND_URL + api_key + "&file=" + url
    if title: req_url += "&title=" + title
    req_url += "&text=" + text if text else "&text="
    if device_id: req_url += "&deviceId=" + device_id
    if device_ids: req_url += "&deviceIds=" + device_ids
    if device_names: req_url += "&deviceNames=" + device_names
    requests.get(req_url)

def send_sms(api_key, sms_number, sms_text, device_id=None, device_ids=None, device_names=None):
    if device_id is None and device_ids is None and device_names is None: return False
    req_url = SEND_URL + api_key + "&smsnumber=" + sms_number + "&smstext=" + sms_text
    if device_id: req_url += "&deviceId=" + device_id
    if device_ids: req_url += "&deviceIds=" + device_ids
    if device_names: req_url += "&deviceNames=" + device_names
    requests.get(req_url)

