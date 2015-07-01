import os, glob
import numpy as np
import matplotlib.pyplot as plt

from funcoes import *


DATADIR = "/home/phellipe/Desktop/uerj-pythoncourse-20150629/sandbox/eduardorichard"
NHEADERS = 2
FIGDIR = "/home/phellipe/Desktop/figures"

#===============================================================

def read_header(lines, n=NHEADERS):
    for k in range(n):
        if 'TEMP' in lines[k]:
            variables = lines[k].split()
        if '(C)' in lines[k]:
            units = lines[k].split()

    return variables, units

def read_data(lines, n=NHEADERS):
    cond, temp, pres, salt = [], [], [], []

    for line, count in zip(lines, range(len(lines))):
        if count in range(n):
            continue

        cond.append( float(line.split(',')[0] ) )
        temp.append( float(line.split(',')[1] ) )
        pres.append( float(line.split(',')[2] ) )
        salt.append( float(line.split(',')[3] ) )

    cond = np.array(cond)
    temp = np.array(temp)
    salt = np.array(salt)
    pres = np.array(pres)

    return cond, temp, salt, pres


filelist = glob.glob( os.path.join(DATADIR, '*.txt') )

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)


for filename in filelist:
    print "Reading and plotting " + filename.split('/')[-1]

    f = open(filename)
    lines = f.readlines()

    variables, units = read_header(lines)
    cond, temp, salt, pres = read_data(lines)

    plot_profiles(cond, temp, salt, pres, filename, FIGDIR)

