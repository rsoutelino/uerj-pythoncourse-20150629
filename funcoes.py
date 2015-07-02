import os, sys
import matplotlib.pyplot as plt


def div(numerador=8, denominador=2):
    """
    Faz uma divisao simples
    numerador   :    o numerador da fracao
    denominador :    o denominador da fracao
    """
    return numerador/denominador


def plot_profiles(cond, temp, salt, pres, filename, savedir):
    """
    Escrever docstring
    INPUT: 
        cond: blaa blaa
    OUTPUT: 
        graphs are genarated and seved at "savedir"
    """
    plt.figure(figsize=(10,5))
    
    plt.subplot(131)
    plt.plot(temp, -pres)
    plt.title('Temperature')

    plt.subplot(132)
    plt.plot(salt, -pres)
    plt.title('Salinity')
    
    if sys.platform == 'win32' or sys.platform == 'win64':
        figname = filename.split('\\')[-1].replace('txt', 'png')
    else:
        figname = filename.split('/')[-1].replace('txt', 'png')

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