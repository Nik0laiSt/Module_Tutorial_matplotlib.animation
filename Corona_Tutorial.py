"""
Matplotlib Animation Example

author: Nikolai Steffan
email: wi20014@lehre.dhbw-stuttgart.de
website: https://github.com/Nik0laiSt
license: MIT
This Code can be used and modified.The only requirement is to keep the above information. Thanks!
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import datetime as dt
import matplotlib.dates as mdates

# First Step is to prepare the data by reading the CSV file into a dataframe
print("importing data...")
df = pd.read_csv("src/data.csv").sort_index(ascending=False)
print("Done!")
# Separieren der Daten für die unterschiedlichen Länder
print("preparing data...")
df_ger = df[df['geoId'] =="DE"] 
df_usa = df[df['geoId'] =="US"] 
df_china = df[df['geoId'] =="CN"] 
df_india = df[df['geoId'] =="IN"] 
print("Done!")

#creating arrays to store plotted data
x_data = []
y_ger_data = []
y_usa_data = []
y_china_data = []
y_india_data = []
#prepare data for x-Axis
start = dt.datetime.strptime(df_ger.iloc[0,0], '%d/%m/%Y')
end = dt.datetime.strptime(df_ger.iloc[349,0], '%d/%m/%Y')
days = mdates.drange(start,end,dt.timedelta(days=1))
#configuring figure
fig, ax = plt.subplots()
ax.set_xlim(start,end)
ax.set_ylim(0,max(df["cases"]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=29))
fig.autofmt_xdate()
ax.grid(True)
ax.set_xlabel("Days")
ax.set_ylabel("Daily Cases")


 
def animation_frame(i:int):
    """animation function: iterates through the days, until it reaches len(df)/4 => 350
        y_XXX_data.append(df_XXX.iloc[i,4]) changes the data to new data of index i

    Args:
        i (int): Iterator for every Animaton Frame
    """
    x_data.append(days[i])
    y_ger_data.append(df_ger.iloc[i,4])
    y_usa_data.append(df_usa.iloc[i,4])
    y_china_data.append(df_china.iloc[i,4])
    y_india_data.append(df_india.iloc[i,4])
    #   ax.plot(x_data, y_XXX_data, color="green") 
    #   plots the data onthe graph with x-Coordinate =x_data 
    #   and y-Coordinate= y_XXX_data and sets the color to green 
    ax.plot(x_data, y_ger_data, color="red", label="Germany")
    ax.plot(x_data, y_usa_data, color="gray", label="USA")
    ax.plot(x_data, y_china_data, color="blue", label="China")
    ax.plot(x_data, y_india_data, color="green", label="India")
    if(len(x_data)==1):
        ax.legend(title="Countries")
        

def save_animation(animation: FuncAnimation, path: str):
    """Saves animation to specific Path

    Args:
        animation (FuncAnimation): Animation to be saved
        path (str): specific path where the animation shall be stored
    """
    # save animation to directory
    mpeg_writer=FFMpegWriter(fps=30)
    print("saving...")
    animation.save(path, writer=mpeg_writer)
    print("Done")




def main():
    path = r"animation.mp4" 
    #   calls the animator
    animation = FuncAnimation(fig, func= animation_frame, interval=10, save_count=349)
    #save_animation(animation=animation, path=path)
    #shows the animation
    plt.show()

if __name__ == "__main__":
    main()