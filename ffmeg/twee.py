import tweepy
import re
import os
from PIL import Image, ImageDraw, ImageFont
import cv2
import json
import configparser


class TwitterTimeline():
    def __init__(self, num=30):
        self.num = num

    def illegal_check(self, s):
        ans = []
        for i in s:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or (
                    '0' <= i <= '9') or i == '!' or i == '?' or i == '.' or i == '@' or i == ' ' or i == '/' or i == '\n':
                ans.append(i)
        return ans

    def tweet_reorg(self, t):
        twitter_text = []
        for tweet in t:
            line = list(tweet.text)
            line = self.illegal_check(line)
            for j in range(len(line)):
                if j % 60 == 0: line.insert(j, '\n')
            line = ''.join(line)
            twitter_text.append(line)
        return twitter_text

    def get_data(self, handle):
        error = tweepy.TweepError
        keys = configparser.ConfigParser()
        keys.read('keys')
        auth = tweepy.OAuthHandler(keys.get('auth', 'consumer_key').strip(),
                                   keys.get('auth', 'consumer_secret').strip())
        auth.set_access_token(keys.get('auth', 'access_token').strip(),
                              keys.get('auth', 'access_token_secret').strip())
        api = tweepy.API(auth)
        path = 'tweets/' + handle + '/'
        try:
            timeline = api.user_timeline(handle, count=self.num)
            source = self.tweet_reorg(timeline)
        except tweepy.TweepError as e:
            print("Something is wrong! Here's the default json.")
            with open('Trump_timeline.json','r') as f:
                source = json.loads((f.read()))


        i = 0
        for tweet in source:
        #store = open(handle + '_timeline.json', 'w')
        #store.write(json.dumps(twitter_text))
            ima = Image.open('background.png')
            draw = ImageDraw.Draw(ima)
            # fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
            word = ImageFont.truetype('times.ttf', 20)
            draw.text((50, 200), tweet, font=word, fill='black')
            ima.save(path + str(i) + '.png')
            i += 1
        video = cv2.VideoWriter(handle + '-daily twitter.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), 1 / 3,
                                (654, 811))
        file_list = os.listdir(path)
        for k in file_list:
            filename = path + k
            ima = cv2.imread(filename)
            video.write(ima)
            print(filename)
            
if __name__ == '__main__':
    test = TwitterTimeline()
    test.get_data("Trump")
