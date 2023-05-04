import pandas as pd
import numpy as np
import datetime, time
import csv

file_name = "20230427194655.record"
folder = 'G://test/CANBus/'
filetype = '.csv'
fixgpschassis = pd.read_csv(folder  + 'fixgps' + 'chassis--' + file_name + ".csv",
                            usecols=[1, 2, 3])
# full_gps = pd.read_csv(folder  + 'fixgps' + 'chassis--' + file_name + ".csv")
# fixgpschassis = pd.read_csv('./p02/fixgpschassis--20230419160110.record.csv',
#                             usecols=[1, 2, 3])

data_fixgpschassis = fixgpschassis.iloc[:, 0:3]
data_fixgpschassis = np.array(data_fixgpschassis)
# full_fixgpschassis = full_gps.iloc[:, :]
# full_fixgpschassis = np.array(full_fixgpschassis)
print(data_fixgpschassis.shape)
# print(full_fixgpschassis.shape)

timestamp = data_fixgpschassis[:, 0]
longitude = data_fixgpschassis[:, 2]
latitude = data_fixgpschassis[:, 1]

# delete repettive data
def simplifydata(list1, list2, time):
    timelist = []
    lolist = []
    lalist = []
    for i in range(len(time)):
        if not list1[i] in lolist:
            timelist.append(time[i])
            lolist.append(list1[i])
            lalist.append(list2[i])
        elif not list2[i] in lalist:
            timelist.append(time[i])
            lolist.append(list1[i])
            lalist.append(list2[i])
    timelist = np.array(timelist)
    lolist = np.array(lolist)
    lalist = np.array(lalist)
    return timelist, lolist, lalist


def findstate(lo, la):
    start = [0]
    finish = [1]
    lo_renew = lo
    la_renew = la

    for i in range(len(lo)):  # A1 start
        if la_renew[i] > 38.0081:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # A1 finish
        if lo_renew[i] > 113.6268:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # A2 start
        if lo_renew[i] > 113.6288:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # A2 finish
        if lo_renew[i] > 113.6305:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # D1 start
        if lo_renew[i] > 113.6331:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # D1 finish
        if 113.6331 > lo_renew[i] > 0:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # A3 start
        if 113.6298 > lo_renew[i] > 0:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # A3 finish
        if la_renew[i] > 38.0094:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # A4 start
        if la_renew[i] > 38.0113:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # A4 finish
        if lo_renew[i] > 113.6298:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # L1 start
        if lo_renew[i] > 113.6340:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # L1 finish
        if la_renew[i] > 38.0125:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # L2 start
        if la_renew[i] > 38.0132:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # L2 finish
        if 113.6338 > lo_renew[i] > 0:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R1 start
        if 113.6298 > lo_renew[i] > 0:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R1 finish
        if la_renew[i] > 38.01385:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R2 start
        if la_renew[i] > 38.0147:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R2 finish
        if lo_renew[i] > 113.6297:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R3 start
        if lo_renew[i] > 113.6336:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R3 finish
        if 38.01495 > la_renew[i] > 0:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R4 start
        if 38.0141 > la_renew[i] > 0:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # R4 finish
        if  113.6338 > lo_renew[i] > 0:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # L3 start
        if 113.6298 > lo_renew[i] > 0:
            start.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # L3 finish
        if 38.01295 > la_renew[i] > 0:
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    for i in range(len(lo)):  # finish
        if 38.0073 > la_renew[i] > 0:
            start.append(i)
            finish.append(i)
            lo_renew[0:i] = 0
            la_renew[0:i] = 0
            break
    return start, finish



def time_transform(t):
    real = []
    for x in t:
        d = datetime.datetime.fromtimestamp(x / 1000000000)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
        real.append(str1)
    return real


newtime, newlo, newla = simplifydata(longitude, latitude, timestamp)
d_newlo, d_newla = newlo, newla
startpoint, finishpoint = findstate(d_newlo, d_newla)
start_timestamp = newtime[startpoint]
finish_timestamp = newtime[finishpoint]
# start_index = np.where(timestamp == start_timestamp[:, None])[-1]
# finish_index = np.where(timestamp == finish_timestamp[:, None])[-1]


driving_state = ['Start-A1','A1','A2','D1','A3','A4',
                 'L1','L2','R1','R2','R3','R4','L3','End']

start_time = time_transform(start_timestamp)
finish_time = time_transform(finish_timestamp)

print(start_time)
print(finish_time)

field = ['state', 'start_time', 'finish_time', 'start_timestamp', 'finish_timestamp', 'duration']
f_timedivision = open(folder  + 'timedivision--' + file_name + ".csv", 'w', newline='')
writer_timedivision = csv.writer(f_timedivision)
writer_timedivision.writerow(field)

for i in range(len(finish_time)):
    time1 = datetime.datetime.strptime(start_time[i], "%Y-%m-%d %H:%M:%S.%f")
    time2 = datetime.datetime.strptime(finish_time[i], "%Y-%m-%d %H:%M:%S.%f")
    duration = (time2 - time1).total_seconds()
    row = [driving_state[i], start_time[i], finish_time[i], start_timestamp[i], finish_timestamp[i], duration]
    writer_timedivision.writerow(row)

f_timedivision.close()




