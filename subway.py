import csv
import matplotlib.pyplot as plt
import numpy as np

f = open('202210subway.csv')
data = csv.reader(f)
next(data)
next(data)

# 4호선 데이터만 출력
# for row in data:
#     for i in range(4, len(row) - 1):
#         row[i] = int(row[i].replace(',', ''))
#     if row[1] == '4호선':
#       print(row)

# 출근시간대 사람이 제일 많은 역
# mx = 0
# mx_station = ''
# for row in data:
#     for i in range(4, len(row) - 1):
#         row[i] = int(row[i].replace(',', ''))
#     if row[1] == '4호선':
#         if sum(row[11:16:2]) > mx:
#             mx = sum(row[11:16:2])
#             mx_station = row[3] + '' + row[1]
#
# print(mx_station, mx)

# t = int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요? :'))
# mx = 0
# mx_station = ''
# for row in data:
#     for i in range(4, len(row) - 1):
#         row[i] = int(row[i].replace(',', ''))
#     a = row[4+(t-4)*2]
#     if row[1] == '4호선':
#         if a > mx:
#             mx = a
#             mx_station = row[3] + '' + row[1]
#
# print(mx_station, mx)

import pandas as pd
s_in = [0] * 24
s_out = [0] * 24
rates = []
for row in data:
    for i in range(4, len(row) - 1):
        row[i] = int(row[i].replace(',', ''))
    for i in range(4, len(row) - 1, 2):
        if row[1] == '4호선':
          if row[i] != 0:
            rate = row[i] / (row[i] + row[i + 1])
            # print(row[1]+row[3], '승하차 비율:', round(rate*100, 2))
            rates.append(np.round(rate*100, 2))
    for k in range(24):
        s_in[k] += row[4+k*2]
        s_out[k] += row[5+k*2]



stations = ['당고개', '상계', '노원', '창동', '쌍문']
times = ['4~5', '5~6', '6~7', '7~8', '8~9']
plt.plot(rates, label='승차비율')
plt.title('시간대별 4호선 승차비율')
plt.rc('font', family = 'Malgun Gothic')
plt.xticks(range(5), stations)
plt.yticks(range(5), times)
plt.legend
