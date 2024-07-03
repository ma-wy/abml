#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import urx 
import numpy

rob = urx.Robot("169.254.162.54")
rob.set_payload(2, (0, 0, 0.1))
rob.set_tcp((0, 0, 0, 0, 0, 0))
#rob.set_tcp((0, 0, 0.265, 0, 0, 0))
a = 0.2
v = 0.3 
print('before movement')
print(rob.getl(wait=True))
joints = [0.034323569387197495, -1.0026090780841272, 2.2072043418884277, -4.346822206174032, -1.6021469275103968, 0.5429958701133728]
rob.movej(joints, acc=a, vel=v, wait=True, relative=False, threshold=None)
print('after movement')
print(rob.getl(wait=True))
rob.close()
