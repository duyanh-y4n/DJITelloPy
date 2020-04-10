#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File            : StreamController_tello_edu.py
# Author          : Duy Anh Pham <duyanh.y4n.pham@gmail.com>
# Date            : 02.04.2020
# Last Modified By: Duy Anh Pham <duyanh.y4n.pham@gmail.com>
'''
StreamController for Tello_edu
'''

from djitellopy.realtime_plot.StreamController import *

if __name__ == "__main__":
    stream_controller = StreamController(topic='tello_edu')
    stream_controller.flush_all_database()
    stream_controller.listen()
