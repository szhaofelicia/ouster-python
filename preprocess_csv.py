import os
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from collections import defaultdict

fps=20
npoints=16384
nchannel=16

frame=1

inputpath='/media/felicia/Data/ouster_data/-1024x10'
framefile='-1024x10 (Frame %s).csv'

dir_list=os.listdir(inputpath)

lidar_df=pd.read_csv(os.path.join(inputpath,framefile%"{:04d}".format(frame)),header=0)

xyz_df=lidar_df[["Point:0","Point:1","Point:2","Channel","Raw Timestamp"]]
xyz_values=xyz_df.values
xyz_np=xyz_df.values.reshape((-1,16,5))

xyz_base=np.ma.masked_equal(xyz_np, 0).mean(axis=1)
timestamp=np.ma.masked_equal(xyz_base[:,-1], 0).mean(axis=0)

xy_sigma=[]
xy_nn=[]
for i in range(1024):
    positions=xyz_np[i,:,:2] # x,y
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(positions)
    dists, idxs = nbrs.kneighbors(positions)
    xy_sigma.append(dists[:,1])
    xy_nn.append(positions[idxs[:,1]])

xy_sigma=np.array(xy_sigma)
xy_nn=np.array(xy_nn)

sigmas=[]
for i in np.arange(0,1,0.1):
    sigmas.append(np.quantile(xy_sigma,i))

sigma=sigmas[6]

xy_positions=xyz_np[:,:,:2]
xy_proj=[]
proj_dict=defaultdict(list)
for i in range(1024):
    ox,oy=xy_positions[i,0]
    temp=[[ox,oy,i,0]]
    for j in range(1,16):
        x,y=xy_positions[i,j]
        dist=np.linalg.norm([ox-x,oy-y])
        if dist < sigma:
            temp.append([ox,oy,i,j])
            ox,oy,_,_=np.mean(temp,axis=0)
        else:
            xy_proj.append([ox,oy])
            
            for ele in temp:
                _,_,idxi,idxj=ele
                proj_dict[(ox,oy)].append([idxi,idxj])
            ox,oy=x,y
            temp=[[ox,oy,i,j]]      
xy_proj=np.array(xy_proj)
xy_radius=np.linalg.norm(xy_proj,axis=1)   



xy_nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(xy_proj)
dists, idxs = xy_nbrs.kneighbors(xy_proj)
xy_delta=dist[:,1]

z_sigma=[]
for x,y in xy_proj:
    idxs=proj_dict[[x,y]]
    z_nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(xyz_np[idxs][2])
    dists, idxs = z_nbrs.kneighbors(xyz_np[idxs][2])
    z_sigma.append(dists[:,1])
z_sigma=np.array(z_sigma)

plt.scatter(xy_proj[:,0], xy_proj[:,1],s=1,c=xy_radius alpha=.5,cmap='viridis')
plt.grid()
plt.colobar
plt.show((16,8))

