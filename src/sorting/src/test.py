#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

num = '1'
save_path = os.path.join('/home/abml/zoe_data/sorting/', num)
print(save_path)
files = os.listdir(save_path)#glob.glob('/home/abml/zoe_data/sorting/1/')#+'*'
print(files)
'''
for f in files:
  print(f)
  os.remove(f)
print('folder: ' + str(folder_path))
print('files: ' + str(len(files)))
print('the folder has been emptied.')
'''
