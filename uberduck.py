import os
from dotenv import load_dotenv
import requests
import urllib.request
from requests.structures import CaseInsensitiveDict
import json
import time
import wave


# python wrapper for uberduck api
class Uberduck:
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('uberduck_key')
        self.secret = os.getenv('uberduck_secret')
        #self.auth = (self.key, self.secret)
        self.auth = os.getenv('uberduck_auth_token')
        self.base_url = "https://api.uberduck.ai/speak"
        self.endpoint_url = "https://api.uberduck.ai/speak-status?uuid="

    # return a wav file from uberduck
    def synth_voice(self, msg, voice):
        uuid = self.request(msg, voice)
        path = self.poll(uuid)
        filename = f'{voice}-{uuid}.wav'
        wave_file = self.download_wav(path, filename)
        return wave_file
                
    # make a request to uberduck api like this
    # curl -u $API_KEY:$API_SECRET \
    # https://api.uberduck.ai/speak \
    # --data-raw '{"speech":"This is just a test.","voice":"eminem"}'
    # return the uuid of the request
    def request(self, speech, voice):
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Authorization"] = f'Basic {self.auth}'
        data = f'{{"speech":"{speech}","voice":"{voice}"}}'
        #data = '{"speech":"This is just a test.","voice":"eminem"}'
        print(data)
        resp = requests.post(self.base_url, headers=headers, data=data)
        print(resp)
        return resp.json()["uuid"]

    # poll the status of the request and return the path to the wav file
    def poll(self, uuid):
        url = f"{self.endpoint_url}{uuid}"
        print(f'polling {url}')
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f'Basic {self.auth}'
        # poll the status of the request
        while True:
            resp = requests.get(url, headers=headers)
            print(resp)
            if resp.json()["path"] != None:
                return resp.json()["path"]
            else:
                print(f'waiting for {url}')
                time.sleep(1)
        # resp = requests.get(url, headers=headers)
        # print(f'Response: {resp}')
        # path = resp.json()["path"]
        # return path

    # download the wav filename from the url
    def download_wav(self, path, filename="test.wav"):
        file_path = ".\\voice_files\\" + filename
        with urllib.request.urlopen(path) as respone:
            with open(filename, 'wb') as f:
                f.write(respone.read())
        return filename


