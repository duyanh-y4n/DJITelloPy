#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File            : live_visualisation.py
# Author          : Duy Anh Pham <duyanh.y4n.pham@gmail.com>
# Date            : 10.04.2020
# Last Modified By: Duy Anh Pham <duyanh.y4n.pham@gmail.com>

from djitellopy.realtime_plot.RealtimePlotter import *
import redis
import numpy as np
import traceback


# define data to get from db
sensorMeshList = ['baro', 'h', 'tof', 'runtime']
row = len(sensorMeshList)
data_len = 200
plot_update_interval = 0.005

option = DataplotOption.TIMESTAMP_CUSTOM
dataplot = DataPlot(row, data_len, option=option)

realtimeplotter = RealtimePlotter(dataplot)

datasource = redis.StrictRedis(host='localhost', port=6379, db=0)


fig, axes = plt.subplots()
plt.title('Data Live Stream with redis')
# plt.show()

realtimeplotter.config_plots(axes, y_labels=sensorMeshList, ylim=[0, 70])

if __name__ == "__main__":
    while True:
        # clear all cached (inc. corrupted data)
        realtimeplotter.dataplot.clear_data_regs()

        # get new data from database
        new_data = []
        for sensor in sensorMeshList:
            new_sensor_data = datasource.lrange(sensor, 0, data_len)
            # reverse, bc first element is the newest (not the oldest like deque)
            new_sensor_data.reverse()
            # print(sensor + ':')
            # print(new_sensor_data)
            new_data.append(new_sensor_data)
        # print(np.array(new_data, dtype=np.float))

        # plot data
        try:
            if realtimeplotter.dataplot.option == DataplotOption.TIMESTAMP_NONE:
                new_data = np.array(new_data, dtype=np.float)
                realtimeplotter.dataplot.append(
                    new_data, single=False)
            elif realtimeplotter.dataplot.option == DataplotOption.TIMESTAMP_CUSTOM:
                y = np.array(new_data[:-1], dtype=np.float)
                x = np.array(new_data[-1], dtype=np.int64)
                realtimeplotter.dataplot.append(
                    y=y, x=x, single=False)
            realtimeplotter.plot_data()
        except Exception as e:
            print(e)
        plt.pause(plot_update_interval)
    input("Exit(press any key)?")
