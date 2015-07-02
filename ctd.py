# -*- coding: utf-8 -*-
import os, glob, argparse
import numpy as np
import matplotlib.pyplot as plt

from funcoes import *


parser = argparse.ArgumentParser(description=u'Lê e plota dados de CTD.')
parser.add_argument('directory', metavar='directory', type=str,
                   help='Nome do diretorio: Ex: [fernanda, eduardorichard]')
parser.add_argument('extension', metavar='extension', type=str,
                   help='Extensao do arquivo: [txt, csv]')
parser.add_argument('-p', '--pres_col', type=int,
                   help='Coluna na qual a pressao se encontra: [0, 2]')
parser.add_argument('-t', '--temp_col', type=int,
                   help='Coluna na qual a temperatura se encontra: [2, 1]')
parser.add_argument('-s', '--salt_col', type=int,
                   help='Coluna na qual a salinity se encontra: [5, 3]')
parser.add_argument('-sep', '--separator', type=str,
                   help='Separador de colunas: [; or ,]')
args = parser.parse_args()

DATADIR = "/home/phellipe/Desktop/uerj-pythoncourse-20150629/sandbox/%s" %(args.directory)
NHEADERS = 2
FIGDIR = "/home/phellipe/Desktop/figures"

#===============================================================


class Cast(object):
    """docstring for Cast"""
    def __init__(self, filename):
        self.filename = filename
        f = open(filename)
        self.lines = f.readlines()

    def split_header_data(self):
        f = open(filename)
        lines = f.readlines()

        temp, pres, salt = [], [], []

        for line in self.lines:
            try: 
                a = float(line.split(args.separator)[0].replace(',', '.'))
                temp.append( float( line.split(args.separator)[args.temp_col].replace(',', '.') ) )
                pres.append( float( line.split(args.separator)[args.pres_col].replace(',', '.') ) )
                salt.append( float( line.split(args.separator)[args.salt_col].replace(',', '.') ) )

            except ValueError:
                if "Start latitude" in line:
                    self.lat = float( line.split(';')[-1].replace(',', '.') )
                if "Start longitude" in line:
                    self.lon = float( line.split(';')[-1].replace(',', '.') )

        self.temp = np.array(temp)
        self.salt = np.array(salt)
        self.pres = np.array(pres)


filelist = glob.glob( os.path.join(DATADIR, '*.%s' %(args.extension)) )

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)

for filename in filelist:
    if "SED" in filename:
        filelist.remove(filename)

for filename in filelist:
    import pdb; pdb.set_trace()
    print "Reading and plotting " + filename.split('/')[-1]
    estacao = Cast(filename)
    estacao.split_header_data()
    plot_profiles(estacao.temp, estacao.salt, 
                  estacao.pres, filename, FIGDIR)

