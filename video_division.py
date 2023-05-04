import os
import ast
import numpy as np
import copy
import calendar
import time
import argparse
import json
import logging
import matplotlib.pyplot as plt
import moviepy.editor
import cv2
import librosa
from envload import *
import datetime
import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import timedelta

video = VideoFileClip('G://test/BL/DJI_20230427195408_0075_D.MP4')
# baseline
# 滴滴声的时间字符串(标准时间已给定)
# 问题：现在以眼动时间计算，实际发现滴滴声代表时间应该更晚
mark_time = '2023-04-27 19:52:35.000'
# 状态开始的时间字符串
start_A2 = '2023-04-27 19:55:11.615974'
# 开始截取的视频时间
time1 = datetime.datetime.strptime(mark_time, "%Y-%m-%d %H:%M:%S.%f")
time2 = datetime.datetime.strptime(start_A2, "%Y-%m-%d %H:%M:%S.%f")
duration = (time2 - time1).total_seconds()

video_start_A1 = duration + 8.61460317  # 滴滴声出现秒数

# 结束截取的视频时间
video_finish_A1 = video_start_A1 + 41.060841  # gps计算每一阶段所用时长

clip = video.subclip(video_start_A1, video_finish_A1)
clip.write_videofile('G://test/BL/PT-jiankong-BL-D1.mp4')






