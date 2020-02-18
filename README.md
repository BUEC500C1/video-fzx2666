# HW4 FFmpeg - Zhou Fang
## Instruction
- First, download all the files and make sure they are all in the same folder.
- Second, use python to execute the file multi_task.py.
```
python multi_task.py
```

## Introduction
- In the file `twee.py`, the function can download 30 most up to date tweets based on the handles given by parameters.
- The function `twitter_data` is called in the multi_task.py. In this file, 3 threads was created to deal with different keywords, which are the handles.
- During the task, the information of the CPU was as below.

- The completed video files were named like `'handle'-daily twitter.avi` and have also been uploaded, including the pictures used to generated those videos. 
- Typically, the size of the video will be about ten times the total size of the pictures. Therefore, this relationship could be used to check whether the video was correctly generated.
