"""
Matplotlib Animation Example

author: Nikolai Steffan
email: wi20014@lehre.dhbw-stuttgart.de
website: https://github.com/Nik0laiSt
license: MIT
This Code can be used and modified.The only requirement is to keep the above information. Thanks!
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# First Step is to prepare the data by reading the CSV file into a dataframe
df = pd.read_csv("data.csv").sort_index(ascending=False)
df_ger = df[df['geoId'] =="DE"] 
df_usa = df[df['geoId'] =="US"] 
df_china = df[df['geoId'] =="CN"] 
df_india = df[df['geoId'] =="IN"] 
print(len(df_china))


x_data = []
y_ger_data = []
y_usa_data = []
y_china_data = []
y_india_data = []
fig, ax = plt.subplots()
ax.set_xlim(0,len(df_ger))
ax.set_ylim(0,max(df["cases"]))
line, = ax.plot(0,0)
leg=ax.legend()
#   animation function: iterates through the days, until it reaches len(df)/4 => 350
#   y_XXX_data.append(df_XXX.iloc[i,4]) changes the data to new data of index i

#   ax.plot(x_data, y_XXX_data, color="green") plots the data onthe graph with x-Coordinate =x_data 
#   and y-Coordinate= y_XXX_data and sets the color to green 

def animation_frame(i):
    
    x_data.append(i)
    y_ger_data.append(df_ger.iloc[i,4])
    y_usa_data.append(df_usa.iloc[i,4])
    y_china_data.append(df_china.iloc[i,4])
    y_india_data.append(df_india.iloc[i,4])

    ax.plot(x_data, y_ger_data, color="red", label="Germany")
    ax.plot(x_data, y_usa_data, color="gray", label="USA")
    ax.plot(x_data, y_china_data, color="blue", label="China")
    ax.plot(x_data, y_india_data, color="green", label="India")

    leg.remove()
    leg=ax.legend()

leg=ax.legend()
#   calls the animator
animation = FuncAnimation(fig, func= animation_frame, interval=10)
plt.show()