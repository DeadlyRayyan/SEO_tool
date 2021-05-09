import requests
from keys import api_key


def channel(channel_id):
    channel_info_raw = requests.get(
        f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}')
    channel_info = channel_info_raw.json()
    channel_info = channel_info['items'][0]['snippet']
    print(channel_info)

def test(channel_id):
    channel_info_raw = requests.get(
        f'https://www.googleapis.com/youtube/v3/channels?part=brandingSettings&id={channel_id}&key={api_key}')
    channel_info = channel_info_raw.json()
    channel_info = channel_info['items']
    print(channel_info)

def main():
    channel_id = input('Channel ID: ')
    test(channel_id)


main()
