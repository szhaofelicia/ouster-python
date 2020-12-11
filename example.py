from os1 import OS1
from os1.utils import xyz_points
# from os1.packet import (
#     AZIMUTH_BLOCK_COUNT,
#     CHANNEL_BLOCK_COUNT,
#     azimuth_angle,
#     azimuth_block,
#     azimuth_measurement_id,
#     azimuth_timestamp,
#     azimuth_valid,
#     channel_block,
#     channel_range,
#     unpack,
# )

def handler(raw_packet):
    """Takes each packet and log it to a file as xyz points"""
    print('Begin writing.')
    with open('points.csv', 'a') as f:
        x, y, z = xyz_points(raw_packet)
        for coords in zip(x, y, z):
            f.write("{}\n".format(','.join(coords)))
        
os1 = OS1('172.24.113.151', '216.165.113.240', mode='1024x20')
os1.start()
os1.run_forever(handler,threaded=True)


"""

AZIMUTH_BLOCK_COUNT, # 16
CHANNEL_BLOCK_COUNT, # 64
azimuth_angle, # <function azimuth_angle at 0x7f8e71f1add0>
azimuth_block, # <function azimuth_block at 0x7f8e71f16b90>
azimuth_measurement_id, # <function azimuth_measurement_id at 0x7f8e71f180e0>
azimuth_timestamp, # <function azimuth_timestamp at 0x7f8e71f16e60>
azimuth_valid, # <function azimuth_valid at 0x7f8e71f1ae60>
channel_block, # <function channel_block at 0x7f8e71f1aef0>
channel_range, # <function channel_range at 0x7f8e71f1af80>
unpack  #<function unpack at 0x7f8e7074d200>

"""