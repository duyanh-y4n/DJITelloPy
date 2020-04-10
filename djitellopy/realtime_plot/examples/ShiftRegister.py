#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File            : shift_register.py
# Author          : Duy Anh Pham <duyanh.y4n.pham@gmail.com>
# Date            : 22.03.2020
# Last Modified By: Duy Anh Pham <duyanh.y4n.pham@gmail.com>

from collections import deque

# -*- coding: utf-8 -*-
"""
    realtime_plot.ShiftRegister
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    example shift register with deque

    :copyright: (c) 2020 by duyanhy4n.
    :license: LICENSE_NAME, see LICENSE for more details.
"""


class ShiftRegister():
    def __init__(self, maxlen=10):
        self.maxlen = maxlen
        self.dataReg = deque(maxlen=maxlen)


test = ShiftRegister(5)
print(test.dataReg)
input()
