import requests
from keys import api_key
from datetime import datetime

keyword = input('Keyword: ')
maxResults = 50


def statistics(videoId, api_key):
    video_info = requests.get(
        f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={videoId}&key={api_key}")
    video_info_array = video_info.json()
    return video_info_array


class Keywords():
    def __init__(self, keyword, num):
        self.keyword = keyword
        self.num = num


class Video():
    def __init__(self, videoId):
        self.videoId = videoId
        self.head = self.head()
        self.tag = self.video_tags()
        self.view = self.view_count()
        self.days = self.days()
        self.score = self.calculate_score()

    def view_count(self):
        video_view_array = statistics(videoId, api_key)
        view_count = video_view_array['items'][0]['statistics']['viewCount']
        view_count_int = int(view_count)
        return view_count_int

    def head(self):
        video_view_array = statistics(videoId, api_key)
        video_title = video_view_array["items"][0]["snippet"]["title"]
        return str(video_title)

    def days(self):
        video_view_array = statistics(videoId, api_key)
        days = video_view_array["items"][0]["snippet"]["publishedAt"]
        days = days[:10]
        date_time_obj = datetime.strptime(days, '%Y-%m-%d')
        today = datetime.today()
        days = today - date_time_obj
        return int(str(days.days))

    def video_tags(self):
        video_view_array = statistics(videoId, api_key)
        try:
            video_tags = video_view_array["items"][0]["snippet"]["tags"]
        except:
            video_tags = 'N/A'
        return video_tags

    def calculate_score(self):
        try:
            score = self.view/self.days
        except ZeroDivisionError as error:
            print('Found a zero error, rounding less than a day to a full day')
            score = self.view / 1

        return score


video = requests.get(
    f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={maxResults}&q={keyword}&type=video&key={api_key}&order=searchSortUnspecified")
video_list = video.json()

print('Processing...')

x = 0
video_container = []

while x != maxResults:

    videoId = video_list["items"][x]["id"]["videoId"]
    video_container.append(Video(videoId))
    x += 1

video_container.sort(key=lambda x: x.score, reverse=True)

print('Showing Results: ')
for y in video_container:
    print(f'{y.head}, https://www.youtube.com/watch?v={y.videoId}, {y.view}, {y.score}')

print('')

print('preparing keywords')
keywords = []

for a in video_container[:5]:
    for words in a.tag:
        work = words
        if work == 'N/A':
            pass
        else:
            work = work.split(',')
            keywords.append(work)

keywords_unique = []

for words in keywords:
    if words in keywords_unique:
        pass
    else:
        keywords_unique.append(words)

keys_container = []

for unique in keywords_unique:
    unique_key = str(unique)
    num = keywords.count(unique)
    keys_container.append(Keywords(unique_key, num))

print(' ')

keys_container.sort(key=lambda x: x.num, reverse=True)
keys_container_final = ''
for keyword in keys_container:
    print(f'{keyword.keyword} occurs {keyword.num} times')
    keys_container_final += (str(keyword.keyword)[2:-2])
    keys_container_final += ', '

print('')
print(keys_container_final)