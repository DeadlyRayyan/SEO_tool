import requests
from keys import api_key

keyword = 'talbina'
maxResults = 20

def statistics(videoId, api_key):
    video_info = requests.get(
        f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={videoId}&key={api_key}")
    video_info_array = video_info.json()
    return video_info_array

class Video():
    def __init__(self, videoId):
        self.videoId = videoId
        self.head = self.head()
        self.tag = self.video_tags()
        self.view = self.view_count()

    def view_count(self):
        video_view_array = statistics(videoId, api_key)
        view_count = video_view_array['items'][0]['statistics']['viewCount']
        view_count_int = int(view_count)
        return view_count_int

    def head(self):
        video_view_array = statistics(videoId, api_key)
        video_title = video_view_array["items"][0]["snippet"]["title"]
        return str(video_title)

    def video_tags(self):
        # tags = requests.get(
        #     f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={videoId}&key={api_key}")
        # tag = tags.json()
        video_view_array = statistics(videoId, api_key)
        try:
            video_tags = video_view_array["items"][0]["snippet"]["tags"]
        except:
            video_tags = 'N/A'
        return video_tags


video = requests.get(
    f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={maxResults}&q={keyword}&type=video&key={api_key}&order=relevance")
video_list = video.json()

x = 0
video_container = []

while x != maxResults:
    videoId = video_list["items"][x]["id"]["videoId"]
    video_container.append(Video(videoId))
    x += 1

# v = video_container[0]
# print(v.videoId)
# print(v.head)
# print(v.view)
# print(v.tag)

video_container.sort(key=lambda x: x.view, reverse=True)

for y in video_container:
    print(f'{y.head}, https://www.youtube.com/watch?v={y.videoId}, {y.view}')

