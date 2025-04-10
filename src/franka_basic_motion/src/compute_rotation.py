#!/usr/bin/env python3.8

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *


q_crr = [0.25987842, 0.25094962, 0.65758415, 0.66111313]
q_rot = angle_axis_to_q_complex(axis = 'x', angle = 2, angle_type = "degree")
q_new = transformation_Q(q_crr,q_rot)
print(q_new)









    
    
    

