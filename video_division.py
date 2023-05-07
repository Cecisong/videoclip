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

timedivision = pd.read_csv('G://P02/7.CANBus/timedivision--20230419160110.record.csv',
                            usecols=[1, 5])
didi_time = pd.read_excel('G://P02/5.RGBs/mark_timestamp.xlsx',usecols=[1])
data_timedivision = timedivision.iloc[:, 0:2]
data_timedivision = np.array(data_timedivision)
didi = didi_time.iloc[:, :]
didi = np.array(didi)
start_time = data_timedivision[-12:,0]
duration = data_timedivision[-12:,1]
state = ['A1','A2','D1','A3','A4',
         'L1','L2','R1','R2','R3','R4','L3']
camera = ['BL', 'D1', 'D2', 'D3', 'P1', 'P2']
file = ['Baseline', 'Driver1', 'Driver2', 'Driver3', 'Passenger1', 'Passenger2']
mark_time = '2023-04-19 16:04:13.701'
time1 = datetime.datetime.strptime(mark_time, "%Y-%m-%d %H:%M:%S.%f")

for i in range(6):
    video = VideoFileClip('G://P02/5.RGBs/' + file[i] + '/P02-' + camera[i] + '.mp4')
    for j in range(len(duration)):
        time2 = datetime.datetime.strptime(start_time[j], "%Y-%m-%d %H:%M:%S.%f")
        relative_duration = (time2 - time1).total_seconds()
        video_start = relative_duration + didi[i]
        video_finish = video_start + duration[j]
        clip = video.subclip(video_start, video_finish)
        clip.write_videofile('G://P02/5.RGBs/clip/P02-'+ camera[i] + '-' + state[j] +'.mp4')






