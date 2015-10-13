# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:09:39 2015

@author: mgordo
This file creates all plots that are not time series (bandwidth, overhead and time) vs (delay, bandwidth, packet loss)
Set paths accordingly, and run script.py, preprocess.py and averaging.py before this script!
"""
import time;
import numpy as np;
import sys
import collections
import matplotlib
from datetime import datetime
import os
import re
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

means=['10', '20', '40', '60', '80', '100', '120']
variances=['0', '10', '20', '40', '50']
losses=['0.0','2.5','5.0']
bandwidths=['1','40','100']
methods=['quic','tcp']
spikes=['0','1']


pathfile=os.path.normpath('C:/Users/Miguel/Desktop/Scientific/processed/')
plotfolder=os.path.normpath('C:/Users/Miguel/Desktop/Scientific/plots/')
#Plots vs packet loss
for mean in means:
    for variance in variances:
        for bandwidth in bandwidths:
            for spike in spikes:
                dicbw={}
                dicoh={}
                dicti={}
                errorbw={}
                erroroh={}
                errorti={}
                err=False
                for method in methods:
                    dicbw[method]=[]
                    dicoh[method]=[]
                    dicti[method]=[]
                    errorbw[method]=[]
                    erroroh[method]=[]
                    errorti[method]=[]
                    for loss in losses:
                        fichero=os.path.normpath(pathfile+'/AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt')
                        try:                        
                            with open(fichero,'r') as f:
                                line=f.readline()
                                parts=line.split()
                                dicbw[method].append(float(parts[2])*8) 
                                dicoh[method].append(float(parts[0])/1000000)                                
                                dicti[method].append(float(parts[1]))
                                line=f.readline()    
                                parts=line.split()
                                errorbw[method].append(float(parts[2])*8)                                
                                erroroh[method].append(float(parts[0])/1000000)
                                errorti[method].append(float(parts[1]))
                        except Exception as error:
                            err=True
                            print('File AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt not found')
                    #Here plotting takes place
                if(not err):
                    plt.figure(figsize=(8,5))
                    plt.errorbar(losses,dicbw[methods[0]],yerr=errorbw[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(losses,dicbw[methods[1]],yerr=errorbw[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Packet Loss (%)')                    
                    plt.ylabel('Throughput (Mbps)')
                    plt.title('Throughput Comparison against packet loss: Delay '+mean+' ms, Variance '+variance+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/BWVSLOSSAVGPLOT_'+bandwidth+'_'+mean+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(losses,dicoh[methods[0]],yerr=erroroh[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(losses,dicoh[methods[1]],yerr=erroroh[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Packet Loss (%)')
                    plt.ylabel('Overhead (MB)')
                    plt.title('Overhead Comparison against packet loss: Delay '+mean+' ms, Variance '+variance+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/OHVSLOSSAVGPLOT_'+bandwidth+'_'+mean+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(losses,dicti[methods[0]],yerr=errorti[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(losses,dicti[methods[1]],yerr=errorti[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Packet Loss (%)')
                    plt.ylabel('Total time for transfer (s)')
                    plt.title('Time transfer Comparison vs packet loss: Delay '+mean+' ms, Variance '+variance+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/TIVSLOSSAVGPLOT_'+bandwidth+'_'+mean+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    
                    
#Plots vs delay                  
for variance in variances:
    for bandwidth in bandwidths:
        for spike in spikes:
            for loss in losses:
                dicbw={}
                dicoh={}
                dicti={}
                errorbw={}
                erroroh={}
                errorti={}
                err=False
                for method in methods:
                    dicbw[method]=[]
                    dicoh[method]=[]
                    dicti[method]=[]
                    errorbw[method]=[]
                    erroroh[method]=[]
                    errorti[method]=[]
                    
                    for mean in means:
                        fichero=os.path.normpath(pathfile+'/AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt')
                        try:                        
                            with open(fichero,'r') as f:
                                line=f.readline()
                                parts=line.split()
                                dicbw[method].append(float(parts[2])*8) 
                                dicoh[method].append(float(parts[0])/1000000)                                
                                dicti[method].append(float(parts[1]))
                                line=f.readline()    
                                parts=line.split()
                                errorbw[method].append(float(parts[2])*8)                                
                                erroroh[method].append(float(parts[0])/1000000)
                                errorti[method].append(float(parts[1]))                                    
                                    
                        except Exception as error:
                            err=True
                            print('File AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt not found')
                    #Here plotting takes place
                            
                if(not err):
                    plt.figure(figsize=(8,5))
                    plt.errorbar(means,dicbw[methods[0]],yerr=errorbw[methods[0]],fmt="x-" ,label="QUIC")
                    plt.errorbar(means,dicbw[methods[1]],yerr=errorbw[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Delay (ms)')                    
                    plt.ylabel('Throughput (Mbps)')
                    plt.title('Throughput Comparison vs delay: Ploss '+loss+'%, Variance '+variance+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/BWVSDELSAVGPLOT_'+bandwidth+'_'+loss+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(means,dicoh[methods[0]],yerr=erroroh[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(means,dicoh[methods[1]],yerr=erroroh[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Delay (ms)')
                    plt.ylabel('Overhead (MB)')
                    plt.title('Overhead Comparison vs delay: Ploss '+loss+'%, ms, Variance '+variance+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/OHVSDELSAVGPLOT_'+bandwidth+'_'+loss+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(means,dicti[methods[0]],yerr=errorti[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(means,dicti[methods[1]],yerr=errorti[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Delay (ms)')
                    plt.ylabel('Total time for transfer (s)')
                    plt.title('Time transfer Comparison vs delay: Ploss '+loss+'%, ms, Variance '+variance+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/TIVSDELSAVGPLOT_'+bandwidth+'_'+loss+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    
#Plots vs bandwidth
for mean in means:
    for variance in variances:
        for spike in spikes:
            for loss in losses:
                dicbw={}
                dicoh={}
                dicti={}
                errorbw={}
                erroroh={}
                errorti={}
                err=False
                for method in methods:
                    dicbw[method]=[]
                    dicoh[method]=[]
                    dicti[method]=[]
                    errorbw[method]=[]
                    erroroh[method]=[]
                    errorti[method]=[]
                    for bandwidth in bandwidths:
                        fichero=os.path.normpath(pathfile+'/AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt')
                        try:                        
                            with open(fichero,'r') as f:
                                
                                line=f.readline()    
                                parts=line.split()
                                dicbw[method].append(float(parts[2])*8) 
                                dicoh[method].append(float(parts[0])/1000000)                                
                                dicti[method].append(float(parts[1]))                                    
                                line=f.readline()    
                                parts=line.split()
                                errorbw[method].append(float(parts[2])*8)                                
                                erroroh[method].append(float(parts[0])/1000000)
                                errorti[method].append(float(parts[1]))
                        except Exception as error:
                            err=True
                            print('File AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt not found')
                #Here plotting takes place
                            
                if(not err):
                    plt.figure(figsize=(8,5))
                    plt.errorbar(bandwidths,dicbw[methods[0]],yerr=errorbw[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(bandwidths,dicbw[methods[1]],yerr=errorbw[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Bandwidth (Mbps)')                    
                    plt.ylabel('Throughput (Mbps)')
                    plt.title('Throughput Comparison vs Bandwidth: Ploss '+loss+'%, Variance '+variance+' ms, Delay '+mean+' ms, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/BWVSBWSAVGPLOT_'+loss+'_'+mean+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(bandwidths,dicoh[methods[0]],yerr=erroroh[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(bandwidths,dicoh[methods[1]],yerr=erroroh[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Bandwidth (Mbps)')
                    plt.ylabel('Overhead (MB)')
                    plt.title('Overhead Comparison vs delay: Ploss '+loss+'%, ms, Variance '+variance+' ms, Delay '+mean+' ms, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/OHVSBWSAVGPLOT_'+loss+'_'+mean+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(bandwidths,dicti[methods[0]],yerr=errorti[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(bandwidths,dicti[methods[1]],yerr=errorti[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Bandwidth (Mbps)')
                    plt.ylabel('Total time for transfer (s)')
                    plt.title('Time transfer Comparison vs delay: Ploss '+loss+'%, ms, Variance '+variance+' ms, Delay '+mean+' ms, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/TIVSBWSAVGPLOT_'+loss+'_'+mean+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                
                        
                    
#Plots vs variance
for mean in means:
    for bandwidth in bandwidths:
        for spike in spikes:
            for loss in losses:
                dicbw={}
                dicoh={}
                dicti={}
                errorbw={}
                erroroh={}
                errorti={}
                err=False
                for method in methods:
                    dicbw[method]=[]
                    dicoh[method]=[]
                    dicti[method]=[]
                    errorbw[method]=[]
                    erroroh[method]=[]
                    errorti[method]=[]
                    
                    for variance in variances:
                        fichero=os.path.normpath(pathfile+'/AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt')
                        try:                        
                            with open(fichero,'r') as f:
                                line=f.readline()
                                parts=line.split()
                                dicbw[method].append(float(parts[2])*8) 
                                dicoh[method].append(float(parts[0])/1000000)                                
                                dicti[method].append(float(parts[1]))
                                line=f.readline()    
                                parts=line.split()
                                errorbw[method].append(float(parts[2])*8)                                
                                erroroh[method].append(float(parts[0])/1000000)
                                errorti[method].append(float(parts[1]))                                    
                                    
                        except Exception as error:
                            err=True
                            print('File AVGDATA'+method+'_'+bandwidth+'_'+loss+'_'+mean+'_'+variance+'_'+spike+'.txt not found')
                    #Here plotting takes place
                            
                if(not err):
                    plt.figure(figsize=(8,5))
                    plt.errorbar(variances,dicbw[methods[0]],yerr=errorbw[methods[0]],fmt="x-" ,label="QUIC")
                    plt.errorbar(variances,dicbw[methods[1]],yerr=errorbw[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Variance (ms)')                    
                    plt.ylabel('Throughput (Mbps)')
                    plt.title('Throughput Comparison vs delay: Ploss '+loss+'%, Delay '+mean+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/BWVSVARSAVGPLOT_'+bandwidth+'_'+loss+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(variances,dicoh[methods[0]],yerr=erroroh[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(variances,dicoh[methods[1]],yerr=erroroh[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Variance (ms)')
                    plt.ylabel('Overhead (MB)')
                    plt.title('Overhead Comparison vs delay: Ploss '+loss+'%, ms, Delay '+mean+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/OHVSVARSAVGPLOT_'+bandwidth+'_'+loss+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    plt.figure(figsize=(8,5))
                    plt.errorbar(variances,dicti[methods[0]],yerr=errorti[methods[0]],fmt="x-", label="QUIC")
                    plt.errorbar(variances,dicti[methods[1]],yerr=errorti[methods[1]],fmt="x-", label="TCP")
                    plt.xlabel('Variance (ms)')
                    plt.ylabel('Total time for transfer (s)')
                    plt.title('Time transfer Comparison vs delay: Ploss '+loss+'%, ms, Delay '+mean+' ms, Bandwidth '+bandwidth+' Mbps, with '+('no ' if int(spike)==0 else '' )+'spikes');
                    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                    rutafigura=os.path.normpath(plotfolder+'/TIVSVARSAVGPLOT_'+bandwidth+'_'+loss+'_'+variance+'_'+spike+'.png')
                    plt.savefig(rutafigura,dpi=150,bbox_inches='tight')#, ,dpi=300
                    
                    
                        
                        
                        
                        
                        
                        
                        
                        
        