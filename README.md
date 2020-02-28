# HW4 FFmpeg - Zhou Fang
## Instruction
- First, download all the files and make sure they are all in the same folder.
- Second, use python to execute the file multi_task.py.
```
python multi_task.py
```
- Note: In the `twee.py` file, the `configparser` function will strip twitter keys from config file. You should replace the empty `keys` file in the project with your own. The format of the config file should be like following:
```
[auth]
consumer_key = ******
consumer_secret = ******
access_token = ******
access_token_secret = ******
```

## Introduction
- In the file `twee.py`, the function can download 30 most up to date tweets based on the handles given by parameters.
- The function `twitter_data` is called in the multi_task.py. In this file, 3 threads was created to deal with different keywords, which are the handles.
- During the task, the information of the CPU was as below.
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-fzx2666/blob/master/CPU-info.png" width= 400>
 </p>
 
- This information could be seen by using `top` command in Linux system.

- The completed video files were named like `'handle'-daily twitter.avi` and have also been uploaded, including the pictures used to generated those videos. 
- Typically, the size of the video will be about ten times the total size of the pictures. Therefore, this relationship could be used to check whether the video was correctly generated.
- As for the background, a blank white picture was used in this task so that words could be read more clearly.

## Error Handling
- If something goes wrong while using tweepy `timeline` function, the program will use the default .json file to create the rest of the process. And it will print out an error message like this:
```
"Something is wrong! Here's the default output."
```
