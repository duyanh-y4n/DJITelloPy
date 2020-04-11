#!/usr/bin/env python3
# File            : export_sensor_data.py
# Author          : Duy Anh Pham <duyanh.y4n.pham@gmail.com>
# Date            : 11.04.2020
# Last Modified By: Duy Anh Pham <duyanh.y4n.pham@gmail.com>
# redis tello export csv
import redis
import numpy as np
import pandas
export_file = '../test_report/Takeoff_Land_Test.csv'
sensor_data_col = ['baro', 'tof', 'h', 'runtime']
sensor_data_types = {'baro':float, 'tof':int, 'h':int, 'runtime':int}
max_data_len = 500

redis = redis.StrictRedis(host='localhost', port=6379, db=0)
keys = redis.keys('*')
data = {}
for i in range(len(keys)):
    keys[i] = keys[i].decode('ASCII')
    data[keys[i]] = np.char.decode(redis.lrange(keys[i], 0, max_data_len))
dataframe = pandas.DataFrame(data)
dataframe = dataframe.astype(sensor_data_types)
dataframe[sensor_data_col].to_csv(export_file)
# dataframe[sensor_data_col].info()
