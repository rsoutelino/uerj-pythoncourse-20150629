import os, glob
import numpy as np
import matplotlib.pyplot as plt

from funcoes import *


DATADIR = "/home/phellipe/Desktop/uerj-pythoncourse-20150629/sandbox/eduardorichard/"
NHEADERS = 2
FIGDIR = "/home/phellipe/Desktop/figures"

#===============================================================

class Cast(object):
    """docstring for Cast"""
    def __init__(self, filename):
        self.filename = filename
        f = open(filename)
        self.lines = f.readlines()

    def read_header(self, n=NHEADERS):
        for k in range(n):
            if 'TEMP' in self.lines[k]:
                self.variables = self.lines[k].split()
            if '(C)' in self.lines[k]:
                self.units = self.lines[k].split()

    def read_data(self, n=NHEADERS):
        cond, temp, pres, salt = [], [], [], []

        for line, count in zip(self.lines, range(len(self.lines))):
            if count in range(n):
                continue

            cond.append( float(line.split(',')[0] ) )
            temp.append( float(line.split(',')[1] ) )
            pres.append( float(line.split(',')[2] ) )
            salt.append( float(line.split(',')[3] ) )

        self.cond = np.array(cond)
        self.temp = np.array(temp)
        self.salt = np.array(salt)
        self.pres = np.array(pres)


filelist = glob.glob( os.path.join(DATADIR, '*.txt') )

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)

for filename in filelist:
    print "Reading and plotting " + filename.split('/')[-1]
    estacao = Cast(filename)
    estacao.read_header()
    estacao.read_data()
    plot_profiles(estacao.cond, estacao.temp, estacao.salt, 
                  estacao.pres, filename, FIGDIR)

