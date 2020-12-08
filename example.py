from os1 import OS1
from os1.utils import xyz_points


def handler(raw_packet):
    """Takes each packet and log it to a file as xyz points"""
    with open('points.csv', 'a') as f:
        x, y, z = xyz_points(raw_packet)
        for coords in zip(x, y, z):
            f.write("{}\n".format(','.join(coords)))
        
os1 = OS1('172.24.113.151', '216.165.113.240', mode='1024x10')
os1.start()
os1.run_forever(handler)
