import requests
import random
import string
import json

token = ""

def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

def generate_random_email():
    return f"{generate_random_string()}@gmail.com"

def generate_random_password():
    return f"{generate_random_string()}1!"

def generate_random_username():
    return generate_random_string()

def get_token():
    global token
    url = "https://passport.twitch.tv/integrity"
    headers = {
        "Accept": "application/vnd.twitchtv.v3+json",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-us",
        "Api-Consumer-Type": "mobile; Android/1809006",
        "Host": "passport.twitch.tv",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI) tv.twitch.android.app/18.9.0/1809006",
        "X-App-Version": "18.9.0",
        "X-Auth-Action": "register",
        "X-Device-ID": "42d3d880bcc24176b3f94f3c8e99bca0"
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        token = response.json()["token"]
        return token
    else:
        print(f"Failed to get token. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        return None

def register_user():
    global token
    url = "https://passport.twitch.tv/protected_register"
    random_email = generate_random_email()
    random_password = generate_random_password()
    random_username = generate_random_username()
    payload = {
        "birthday": {
            "day": 3,
            "month": 4,
            "year": 1998
        },
        "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
        "email": random_email,
        "include_verification_code": True,
        "integrity_token": token,
        "password": random_password,
        "username": random_username
    }
    headers = {
        "Accept": "application/vnd.twitchtv.v3+json",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-us",
        "Api-Consumer-Type": "mobile; Android/1809006",
        "Client-ID": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
        "Host": "passport.twitch.tv",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI) tv.twitch.android.app/18.9.0/1809006",
        "X-App-Version": "18.9.0",
        "X-Device-ID": "42d3d880bcc24176b3f94f3c8e99bca0"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        with open("login.txt", "w") as f:
            f.write(f"Username: {random_username}\nEmail: {random_email}\nPassword: {random_password}")
    else:
        print(f"Registration failed. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
token = get_token()
if token:
    register_user()
else:
    print("Failed to obtain token.")
