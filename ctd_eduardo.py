import glob
import os
import numpy as np
import matplotlib.pyplot as plt

DATADIR = "/home/phellipe/Desktop/uerj-pythoncourse-20150629/sandbox/eduardorichard"
NHEADERS = 2

#===============================================================

filelist = glob.glob( os.path.join(DATADIR, '*.txt') )

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)


for filename in filelist:
    f = open(filename)
    lines = f.readlines()

    # read headers
    for k in range(NHEADERS):
        if 'TEMP' in lines[k]:
            variables = lines[k].split()
        if '(C)' in lines[k]:
            units = lines[k].split()

    # read data
    cond, temp, pres, salt = [], [], [], []

    for line, count in zip(lines, range(len(lines))):
        if count in range(NHEADERS):
            continue

        cond.append( float(line.split(',')[0] ) )
        temp.append( float(line.split(',')[1] ) )
        pres.append( float(line.split(',')[2] ) )
        salt.append( float(line.split(',')[3] ) )

    cond = np.array(cond)
    temp = np.array(temp)
    salt = np.array(salt)
    pres = np.array(pres)

    # start plotting
    plt.figure(figsize=(10,5))
    
    plt.subplot(131)
    plt.plot(temp, -pres)

    plt.subplot(132)
    plt.plot(salt, -pres)

    plt.subplot(133)
    plt.plot(cond, -pres)

