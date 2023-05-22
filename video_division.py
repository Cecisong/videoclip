import pandas as pd
from envload import *
import datetime
import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import timedelta

test_number = 'P12'

timedivision = pd.read_csv('F://' + test_number+'/7.CANBus/timedivision--20230517160138.record.csv',
                            usecols=[1, 5])
didi_time = pd.read_excel('F://' + test_number+'/5.RGBs/mark_timestamp.xlsx',usecols=[1])
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


mark_time = '2023-05-17 16:09:23.633'
time1 = datetime.datetime.strptime(mark_time, "%Y-%m-%d %H:%M:%S.%f")

for i in range(6):
    video = VideoFileClip('F://' + test_number+'/5.RGBs/' + file[i] + '/' + test_number+'-' + camera[i] + '.mp4')
    for j in range(len(duration)):
        time2 = datetime.datetime.strptime(start_time[j], "%Y-%m-%d %H:%M:%S.%f")
        relative_duration = (time2 - time1).total_seconds()
        video_start = relative_duration + didi[i]
        video_finish = video_start + duration[j]
        clip = video.subclip(video_start, video_finish)
        clip.write_videofile('F://' + test_number+'/5.RGBs/clip/' + test_number+'-'+ camera[i] + '-' + state[j] +'.mp4')






