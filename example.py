from os1 import OS1
from os1.utils import xyz_points


def handler():
    """Takes each packet and log it to a file as xyz points"""
    print("handler!")
    # with open('points.csv', 'a') as f:
    #     x, y, z = xyz_points(raw_packet)
    #     print(x,y,z)
    #     for coords in zip(x, y, z):
    #         f.write("{}\n".format(','.join(coords)))
        
os1 = OS1('172.24.113.151', '10.27.23.132', mode='1024x20') # PC_ethernet: 192.168.0.141, PC VPN:10.27.94.178, lab: 216.165.113.240
os1.start()
os1.run_forever(handler)

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