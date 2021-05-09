import requests
from keys import api_key

keyword = 'talbina'
maxResults = 5


def video_title(videoId):
    views = requests.get(
        f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={videoId}&key={api_key}")
    view = views.json()
    video_title = view["items"][0]["snippet"]["title"]
    return video_title


def video_tags(videoId):
    views = requests.get(
        f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={videoId}&key={api_key}")
    view = views.json()
    try:
        video_tags = view["items"][0]["snippet"]["tags"]
    except:
        video_tags = 'N/A'
    return video_tags


def view_count(videoId):
    views = requests.get(
        f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={videoId}&key={api_key}")
    view = views.json()
    view_count = view['items'][0]['statistics']['viewCount']
    return view_count


class Video():
    def __init__(self, id, head, tag, view):
        self.id = videoId
        self.head = video_title(id)
        self.tag = video_tags(id)
        self.view = view_count(id)


video = requests.get(
    f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={maxResults}&q={keyword}&type=video&key={api_key}&order=relevance")
video_list = video.json()
x = 0
video_container = []

while x != maxResults:
    videoId = video_list["items"][x]["id"]["videoId"]
    channel_title = video_list["items"][x]["snippet"]["channelTitle"]
    video_container.append(videoId)

print(video_container)

# while x != maxResults:
#     videoId = video_list["items"][x]["id"]["videoId"]
#     channel_title = video_list["items"][x]["snippet"]["channelTitle"]
#     title = video_title(videoId)
#     views = view_count(videoId)
#     tags = video_tags(videoId)
#     print(f'{title} - {views} - {tags}')
#     x += 1

print(f'Showing {x} results')
