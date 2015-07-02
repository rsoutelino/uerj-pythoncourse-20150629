import os, sys
import matplotlib.pyplot as plt


def div(numerador=8, denominador=2):
    """
    Faz uma divisao simples
    numerador   :    o numerador da fracao
    denominador :    o denominador da fracao
    """
    return numerador/denominador


def plot_profiles(temp, salt, pres, filename, savedir):
    """
    Escrever docstring
    INPUT: 
        cond: blaa blaa
    OUTPUT: 
        graphs are genarated and seved at "savedir"
    """
    plt.figure(figsize=(10,5))
    
    plt.subplot(121)
    plt.plot(temp, -pres)
    plt.title('Temperature')

    plt.subplot(122)
    plt.plot(salt, -pres)
    plt.title('Salinity')

    if sys.platform == 'win32' or sys.platform == 'win64':
        figname = filename.split('\\')[-1].split('.')[0] + '.png'
    else:
        figname = filename.split('/')[-1].split('.')[0] + '.png'

    figname = os.path.join(savedir, figname)
    print "    --> saving png"
    plt.savefig(figname)