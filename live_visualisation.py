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
import matplotlib


# define data to get from db
# sensorMeshList = ['baro', 'h', 'tof', 'runtime']
# row = len(sensorMeshList)
data_len = 300
plot_update_interval = 0.005
datasource = redis.StrictRedis(host='localhost', port=6379, db=0)

plt.figure()

baro_axes = plt.subplot(3, 1, 1)
plt.title('tello_edu sensors')
baro_data_list = ['baro', 'runtime']
baro_ylim = [-47, -57]
baro_option = DataplotOption.TIMESTAMP_CUSTOM
baro_dataplot = DataPlot(2, data_len, option=baro_option)
baro_plot = RealtimePlotter(baro_dataplot)
baro_plot.config_plots(baro_axes, y_labels=baro_data_list, ylim=baro_ylim)
baro_plot.axes.set_xlabel('time in ms')
baro_plot.axes.set_ylabel('barometer in cmHg')


tof_axes = plt.subplot(3, 1, 2)
tof_data_list = ['tof', 'runtime']
tof_ylim = [-10, 500]
tof_option = DataplotOption.TIMESTAMP_CUSTOM
tof_dataplot = DataPlot(2, data_len, option=tof_option)
tof_plot = RealtimePlotter(tof_dataplot)
tof_plot.config_plots(tof_axes, y_labels=tof_data_list, ylim=tof_ylim)
tof_plot.axes.set_xlabel('time in ms')
tof_plot.axes.set_ylabel('vertical distance in cm')

h_axes = plt.subplot(3, 1, 3)
h_ylim = [-50, 300]
h_data_list = ['h', 'runtime']
h_option = DataplotOption.TIMESTAMP_CUSTOM
h_dataplot = DataPlot(2, data_len, option=h_option)
h_plot = RealtimePlotter(h_dataplot)
h_plot.config_plots(h_axes, y_labels=h_data_list, ylim=h_ylim)
h_plot.axes.set_xlabel('time in ms')
tof_plot.axes.set_ylabel('height in cm')


if __name__ == "__main__":
    while True:
        # get new data from database and plot
        # baro
        baro_plot.dataplot.clear_data_regs()
        new_data = []
        for sensor in baro_data_list:
            new_sensor_data = datasource.lrange(sensor, 0, data_len)
            # reverse, bc first element is the newest (not the oldest like deque)
            new_sensor_data.reverse()
            new_data.append(new_sensor_data)
        try:
            baro_y = np.array(new_data[:-1], dtype=np.float)
            baro_x = np.array(new_data[-1], dtype=np.int64)
            baro_plot.dataplot.append(
                y=baro_y, x=baro_x, single=False)
            baro_plot.plot_data()
        except Exception as e:
            print(e)
        # tof
        tof_plot.dataplot.clear_data_regs()
        new_data = []
        for sensor in tof_data_list:
            new_sensor_data = datasource.lrange(sensor, 0, data_len)
            # reverse, bc first element is the newest (not the oldest like deque)
            new_sensor_data.reverse()
            new_data.append(new_sensor_data)
        try:
            tof_y = np.array(new_data[:-1], dtype=np.float)
            tof_x = np.array(new_data[-1], dtype=np.int64)
            tof_plot.dataplot.append(
                y=tof_y, x=tof_x, single=False)
            tof_plot.plot_data()
        except Exception as e:
            print(e)
        # height
        h_plot.dataplot.clear_data_regs()
        new_data = []
        for sensor in h_data_list:
            new_sensor_data = datasource.lrange(sensor, 0, data_len)
            # reverse, bc first element is the newest (not the oldest like deque)
            new_sensor_data.reverse()
            new_data.append(new_sensor_data)
        try:
            h_y = np.array(new_data[:-1], dtype=np.float)
            h_x = np.array(new_data[-1], dtype=np.int64)
            h_plot.dataplot.append(
                y=h_y, x=h_x, single=False)
            h_plot.plot_data()
        except Exception as e:
            print(e)

        plt.pause(plot_update_interval)
    input("Exit(press any key)?")
