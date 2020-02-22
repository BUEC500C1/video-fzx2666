import tweepy
import re
import os
from PIL import Image, ImageDraw, ImageFont
import numpy
import cv2

def illegalCheck(s):
	ans = []
	for i in s:
		if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9') or i=='!' or i=='?' or i=='.' or i=='@' or i==' ' or i =='/' or i=='\n':
			ans.append(i)
	return ans

def twitter_data(handle):
  [auth]
  consumer_key = ****
  consumer_secret = ****
  access_token = ****
  access_secret = ****
  auth = tweepy.OAuthHandler(consumer_key,secret_key)
  auth.set_access_token(access_token, token_secret)
  api = tweepy.API(auth)

  path = 'tweets/'+ handle+'/'

  timeline = api.user_timeline(handle, count = 30)
  print(len(timeline))

  highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
  i = 0
  for tweet in timeline :
  	line = list(tweet.text)
  	line = illegalCheck(line)
  	for j in range(len(line)):
  		if (j%60==0): line.insert(j,'\n')

  	line = ''.join(line)
  	ima = Image.open('background.png')
  	draw = ImageDraw.Draw(ima)
  	#fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
  	word = ImageFont.truetype('times.ttf', 20)
  	draw.text((50,200), line, font = word, fill = 'black')
  	ima.save(path+str(i) + '.png')
  	i+=1


  video = cv2.VideoWriter(handle+'-daily twitter.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),1/3,(654,811))

  filelist = os.listdir(path)
  for k in filelist:
    filename = path + k
    ima = cv2.imread(filename)
    video.write(ima)
    print(filename)
