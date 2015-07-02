import glob
import os, sys
import numpy as np
import matplotlib.pyplot as plt

savedir = "c:/Users/Camila/Desktop/teste"
DATADIR = "c:/Users/Camila/Desktop/uerj-pythoncourse-20150629/sandbox/eduardorichard"
NHEADERS = 2
print 'aaaaa'

#===============================================================

def read_header(lines, n=NHEADERS):
    for k in range(NHEADERS):
        if 'TEMP' in lines[k]:
            variables = lines[k].split()
        if '(C)' in lines[k]:
            units = lines[k].split()

    return variables, units

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
                print 'wwwwwwww'
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
def plot_profiles(cond, temp, salt, pres, filename, savedir):
    """
    Escrever docstring
    INPUT: 
        cond: blaa blaa
    OUTPUT: 
        graphs are genarated and seved at "savedir"
    """
    print 'ffffffff'
    plt.figure(figsize=(10,5))
    
    plt.subplot(131)
    plt.plot(temp, -pres)
    plt.title('Temperature')

    plt.subplot(132)
    plt.plot(salt, -pres)
    plt.title('Salinity')
    
    if sys.platform == 'win32' or sys.platform == 'win64':
        plt.suptitle(filename.split('\\')[-1])
    else:
        plt.suptitle(filename.split('/')[-1])


    plt.subplot(133)
    plt.plot(cond, -pres)
    plt.title('Conductivity')

    if sys.platform == 'win32' or sys.platform == 'win64':
        figname = filename.split('\\')[-1].replace('txt', 'png')
    else:
        figname = filename.split('/')[-1].replace('txt', 'png')

    figname = os.path.join(savedir, figname)
    print "    --> saving png"
    plt.savefig(figname)

plot_profiles(cond,temp,salt,pres,filename,savedir)
plt.show()