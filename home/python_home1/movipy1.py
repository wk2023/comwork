from moviepy import editor
import os
import random
import math

path = "F:\\video1\\"  # 视频文件夹 一定注意是\\ 双斜杠
video_time = 3
video_lgtime = 12
video_list = []
# print(fiels)

'''
def video_time_list(path, video_time):
    fiels = os.listdir(path)
    video_list = []
    for i in fiels:
        # print(i)
        clips = editor.VideoFileClip('F:\\video1\\'+i)
        # print(clips.duration)
        if clips.duration > video_time:
            video_list.append('F:\\video1\\'+i)
        # print(video_list)
        clips.reader.close()
        clips.audio.reader.close_proc()
    return video_list
'''


def out_video ():
    video_time = 3
    video_lgtime = 12
    bit_number = math.ceil(video_lgtime/video_time)
    print(bit_number)
    for i in bit_number:
        video_list = ['F:\\video1\\1 (2).mp4', 'F:\\video1\\1 (3).mp4', 'F:\\video1\\1 (4).mp4', 'F:\\video1\\1 (5).mp4']
        video_namber = random.randint(0, len(video_list)-1)
        print(video_list[video_namber])
        clips = editor.VideoFileClip(video_list[video_namber])
        video_suijitime = random.randint(0, clips.duration-video_time)
        clips.subclip(video_suijitime, video_suijitime+video_time)
    

'''
video_list = video_time_list(path, video_time)
print(video_list) '''
out_video()