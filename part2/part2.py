# Stanley Gao
# 5/8/22
# Part 2: Free-Form Modeling

import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import pandas as pd
import datetime

plt.style.use('_mpl-gallery')

# make data
df = pd.read_csv("Sample - Superstore.csv", delimiter=',', header='infer', encoding='latin1')
df.index=pd.to_datetime(df['Order Date'])

df = pd.get_dummies(df['Ship Mode'])
# df.rename(columns={'First Class': 'FC', 'Same Day': 'SD', 'Second Class': 'SC', 'Standard Class': 'STDC'}, inplace=True)

df = df.resample('1M').mean()

# plot:

fig = plt.figure(figsize=(10, 5))
ax = plt.axes(ylim=(0, 1))

plt.ylabel('% of Orders')
plt.xlabel('Dates')
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.94, left = 0.12, right = 0.94) #ensuring the dates (on the x-axis) fit in the screen

line1, = ax.plot([],[],lw=2,color="red")
line2, = ax.plot([],[],lw=2,color="green")
line3, = ax.plot([],[],lw=2,color="blue")
line4, = ax.plot([],[],lw=2,color="orange")

def init():
  line1.set_data([],[])
  line2.set_data([],[])
  line3.set_data([],[])
  line4.set_data([],[])
  return line1, line2, line3, line4

def animate(i):
  plt.legend(df.columns, bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
  if i == 0: return
  datearray = df[:i].index
  ax.set_xlim(min(datearray) - datetime.timedelta(days=1), max(datearray) + datetime.timedelta(days=1))
  line1.set_data(datearray, df[:i]['Same Day'].values)
  line2.set_data(datearray, df[:i]['First Class'].values)
  line3.set_data(datearray, df[:i]['Second Class'].values)
  line4.set_data(datearray, df[:i]['Standard Class'].values)
  return line1, line2, line3, line4

animator = ani.FuncAnimation(fig, animate, interval = 100)

animator.save(r"C:\Users\gaost\Dropbox (Dartmouth College)\\22S\dali data challenge\part2_animation.gif")